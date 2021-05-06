# -*- coding: utf-8 -*-

import pandas as pd
import random
import numpy as np
import math
from matplotlib import pyplot as plt
import seaborn as sns
import time
import os.path
import pandas_ta as ta

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
pd.options.display.float_format = '{:,.2f}'.format
plt.rcParams["figure.figsize"] = (20,11.25)

class q:
    def __init__(self):
        self.amountTable = pd.DataFrame(0., index=range(10),columns=range(10))
        self.amountTableLog = pd.DataFrame(columns=['position', 'suggestion', 'amount', 'action'])
        #追蹤決定後X日股價變化作獎勵
        self.renderTail = 50
        #舊記憶衰減率
        self.attenuation = 0.99999
        #前期回合隨機探索減少速度
        self.threshold = 0.
        self.randomRaise = 0.0001
        #追貨獎勵加權（bot動態調整）
        self.greedy = 1.
        #機會成本懲罰加權（bot動態調整）
        self.safe = 1.
        self.saveFile = False
        self.reportDeep = False
        self.plottoPng = False
        self.startTime = time.time() 
        self.greedyLog = pd.DataFrame(columns=['greedy', 'safe' , 'p'])
    def train(self, stock, num):
        history = self.__setHistory__
        clearer = self.amountTableLog.iloc[0:0]
        trade = self.__goTrading__
        finalP = []
        finalM = []
        finalP_append = finalP.append
        finalPosition = []
        finalM_append = finalM.append
        pr = self.print
        n = self.__normalizeQTable__
        hm = self.__heatmap__
        plot = plt.plot
        show = plt.show
        title = plt.title
        for i in range(len(stock)):
            path = ("h/%s.csv" % stock[i])
            h = history(path)
            cash = ( h.at[0, 'close'] * 10 )
            for times in range(num):
                self.amountTableLog = clearer
                final = trade(cash, h)
                p = (final[0] * final[1]) + final[2]
                finalP_append(p)
                finalPosition.append(final[0] * final[1])
                finalM_append(np.mean(finalP))

                self.greedyLog = self.greedyLog.tail(20)
                self.greedyLog = self.greedyLog.append({'greedy' :self.greedy, 'safe': self.safe , 'p' : p}, ignore_index=True)
                idx = self.greedyLog['p'].idxmax()
                ng = self.greedyLog['greedy'].loc[idx] + np.random.normal(0, 0.1, 1)[0]
                sa2 = self.greedyLog['safe'].loc[idx] + np.random.normal(0, 0.1, 1)[0]
                if ng > 0: self.greedy = ng 
                if sa2 > 0: self.safe = sa2
                    
                if (times % 20) == 0:
                    pr('第%s回合｜平均總資產：%s' % ( (times + 1), np.mean(finalP)))
            m = np.mean(finalP)
            rd = "{:0.2f}".format(((m - cash) / cash) * 100)
            
            pr('完結｜平均總資產：%s|回報：%s%%' % (m, rd))
            
            plotTitle = '%s:%s%%' %(stock[i], rd)
            
            title(plotTitle)
            plot(finalP)
            plot(finalM)
            plot(finalPosition, c='grey', linewidth=0.5)
            if self.plottoPng: plt.savefig(self.__plotFileName__())
            else: show()
            plt.clf()
            
            hm(plotTitle, n(self.amountTable), True)
            
            finalP = []
            finalM = []
    def __goTrading__(self, c, d):
        df = d
        cash = c
        holding = 0
        report = self.__genDailyReport__
        getAction = self.__action__
        floor = math.floor
        th = self.threshold
        rr = self.randomRaise

        for i in range(len(df)):
            close = df.at[i, 'close']
            position = holding * close
            p = cash + position
            
            change = 0
            if not i == 0: change = close - df.at[i - 1, 'close']
            
            bHolding = holding
            bCash = cash
            actionCheck = 0

            if not i == (len(df) - 1):
                
                if th < 1 and random.random() > self.threshold: ra = True
                else: ra = False
                action, amount = getAction(cash, position, p, close, change, holding, ra)  
                
                nextOpen = df.at[i + 1, 'open']
                if action == 0 and cash > nextOpen:
                    avaToBuy = floor(cash / nextOpen)
                    if amount > avaToBuy: amount = avaToBuy
                    if cash < (nextOpen * amount): actionCheck = 1
                    else:
                        cash -= (nextOpen * amount)
                        holding += amount
                elif action == 2:
                    if amount > holding: amount = holding
                    if holding == 0: actionCheck = 2
                    cash += (nextOpen * amount)
                    holding -= amount
                else:
                    actionCheck = 3
            else:
                action = 1
            
            if th < 1: self.threshold += rr
            report(i, bCash, action, close, bHolding, actionCheck, nextOpen, position, p, action, amount)
        
        return [df['close'].tail(1).item(), holding, cash]
    def __action__(self, cash, position, portfolio, price, change, holding, ra):
        m = 2
        #無貨時不會作沽貨決定
        if holding == 0: m = 1
        action = random.randint(0, m)
        a = self.__amount__(action, cash, position, portfolio, price, change, holding, ra)
        #倉位拒絕決定後，修改output
        if a == 0: action = 1
        return action, a
    def __amount__(self, action, cash, position, portfolio, price, change, holding, ra):   
        table = self.amountTable
        p_raw = self.amountTableLog.tail(self.renderTail).reset_index(drop=True)
        e = self.greedy
        at = self.attenuation
        safe = self.safe
        floor = math.floor
        
        #讀取決策紀錄，將股價變化轉作獎勵，更新決策表
        for i in range(len(p_raw)):
            op = p_raw['position'].loc[i]
            os = p_raw['suggestion'].loc[i]
            oa = p_raw['action'].loc[i]
            oAmount = p_raw['amount'].loc[i]
            #追貨獎勵
            if oa == 0: reward = (change * oAmount) * e
            #持貨獎勵
            elif oa == 1: reward =  change * oAmount
            #沽貨獎勵
            elif oa == 2: reward = ((change * oAmount) * -1)
            else: self.print('errorWhenCountingAmount')
            #機會成本，避免bot「取勝唯一法︰『及早離去』四字而矣。」
            reward = reward - (((cash / price) * change) * safe)
            self.amountTable.at[op, os] = (table.at[op, os] * at) + reward
        
        #計算倉位
        p = floor((position/ portfolio) * 10)
        if p ==10: p = 9
        
        if action == 1:
            s = p
            a = 0
        else:
            if not len(self.amountTableLog) == 0:
                if action == 0:
                    df = self.amountTable.iloc[p, p:]
                elif action == 2:
                    df = self.amountTable.iloc[p, :(p+1)]
                else:
                    self.print('errorWhenCountingAmount')
                st = pd.to_numeric(df).idxmax()     
            
            if (not 'st' in locals()) or ra or math.isnan(st):
                if action == 0 : 
                    ava = floor(cash / price)
                    if ava <= 2: a = 1
                    else: a = random.randint(1, ava)
                    newHold = holding + a
                elif action == 2:
                    a = random.randint(1, holding)
                    newHold = holding - a
                s = floor(((price * newHold) / portfolio) * 10)
                    
            elif (action == 0) or (action == 2):
                if st == p:
                    s = p
                    a = 0
                else:
                    if action == 0:
                        c = st - p
                    else: c = p - st
                    
                    changelvl = (portfolio / 10) * c
                    if (action == 1) and (changelvl > cash) :changelvl = cash
                    
                    a = floor(changelvl / price)
                    
                    ca = a * price
                    if action == 2 : ca = ca * -1
                    
                    s = floor(((position + ca)/ portfolio) * 10)
            
            else: self.print('errorWhenCountingAmount')
        if s >= 10 : s = 9
        r = a
        if action == 1: r = 0
        self.amountTableLog = p_raw.append({'position' :p , 'suggestion' : s, 'amount' : a, 'action': action}, ignore_index=True)
        return r
    def __setHistory__(self, path):
        df = pd.read_csv(path)
        df = df.dropna()
        df = df.iloc[::-1]
        df = df.reset_index(drop=True)
        sma50 = ta.sma(df["close"], length=50)
        df = pd.concat([df, sma50, ], axis=1)
        df = df[(df['SMA_50'] > 0)]
        df = df.reset_index(drop=True)
        return df
    def __heatmap__(self, title, data, invert = False):
        plt.title(title)
        hm = sns.heatmap(data, linewidth=0.5, cmap="rainbow")
        if invert: hm.invert_yaxis() 
        if self.plottoPng :plt.savefig(self.__plotFileName__())
        else: plt.show()
        plt.clf()
    def __normalizeQTable__(self, df):
        df.fillna(value=0, inplace=True)
        df2 = df.min()
        df2 = pd.to_numeric(df2).min()
        if df2 < 0:
            df2 = df2 * -1
            df = df + df2
        else:
            df = (df / df2) - 1
        df2 = df.max()
        df2 = pd.to_numeric(df2).max()
        df = df / df2
        return df
    def deepReport(self):
        self.reportDeep = True
    def __genDailyReport__(self, day, cash, action, close, holding, actionCheck, nextOpen, position, p, lastAction, lastAmount):
        action_text = ['追', '揸', '沽']
        if self.reportDeep: self.print('第%s日|股價：%s|持倉：%s|市值：%s|現金：%s|總資產：%s|%s：%s股數' % (day, "{:0.2f}".format(close) ,holding, "{:0.2f}".format(position), "{:0.2f}".format(cash), "{:0.2f}".format(p), action_text[action], lastAmount))
    def saveToFile(self):
        self.saveFile = True
        self.t = open("report.txt", "w")
    def print(self, txt):
        if self.saveFile:
            self.t.write(str(txt))
            self.t.write('\n')
        else: print(txt)
    def __plotFileName__(self):
        file = 1
        while os.path.isfile('p/%s.png' % file):
            file += 1
        return ('p/%s.png' % file)
    def __exit__(self):
        if self.saveFile: self.t.close()
    def plotPng(self):
        self.plottoPng = True

#樣本清單
l = ['315', '388', '700', '762', '883', '941', '1137', '2098', '6823', 
     'aapl', 'ccl', 'dis', 'fslr', 'mur', 'sqqq', 'tsla', 'su']

#測試股票
d = ['tsla']

a = q()

#詳細紀錄
#a.deepReport()

#不輸出console，儲存txt
#a.saveToFile()

#圖片不plot到consloe，改為儲存png
#a.plotPng()

#開始訓練，係會load得比較慢，畀啲耐性
print('started')
a.train(d, 500)


