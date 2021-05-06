# -*- coding: utf-8 -*-
# 修改自Predictive Analytics with TensorFlow
# https://github.com/PacktPublishing/Predictive-Analytics-with-TensorFlow
# 所以code有啲亂

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import random
import talib
from talib import abstract
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

#交易class例子

#隨機交易
class RandomDecisionPolicy():
    def __init__(self, actions):
        self.actions = actions

    def select_action(self, current_state):
        action = self.actions[random.randint(0, len(self.actions) - 1)]
        return action

#RSI交易    
class rsiPolicy():
    def __init__(self, actions):
        self.actions = actions

    def select_action(self, c):
        
        rsi = c['RSI_14']
        
        if rsi < 20:
            action = self.actions[0]
        elif rsi > 80:
            action = self.actions[1]
        else:
            action = self.actions[2]
        return action

#MACD交易        
class macdPolicy():
    def __init__(self, actions):
        self.actions = actions
        
    def select_action(self, c):

        macdh = c['macdhist']
        
        if macdh > 0:
            return self.actions[0]
        elif macdh < 0:
            return self.actions[1]
        else:
            return self.actions[2]

#技術指標交易        
class cheatingPolicy():
    def __init__(self, actions):
        self.actions = actions
        
    def select_action(self, c):
        r = flagGen(c)
        buyList = [0, 132, 512, 4]
        sellList = [999, 867, 487, 995, 66535]
        if r in buyList: 
            return self.actions[0]
        if r in sellList: 
            return self.actions[1]
        return self.actions[2]
        
def flagGen(d):
    #加入指標
    #以二進制度保持指標狀態
    l = [
        (d['close'] > d['SMA_5']),  
        (d['SMA_5'] > d['SMA_10']), 
        (d['SMA_10'] > d['SMA_50']), 
        (d['RSI_14'] > 80),
        (d['RSI_14'] < 20),
        (d['SMA_5_u'] > 0),
        (d['SMA_10_u'] > 0),
        (d['SMA_50_u'] > 0),
        (d['macdhist'] > 0),
        (d['macdhist_u'] > 0),
        (d['close'] > d['upper']),
        (d['lower'] > d['close']),
        (d['CDLABANDONEDBABY'] > 0),
        (d['CDLABANDONEDBABY'] < 0),
        (d['CDLADVANCEBLOCK'] > 0),
        (d['CDLADVANCEBLOCK'] < 0),
        (d['CDLCLOSINGMARUBOZU'] > 0),
        (d['CDLCLOSINGMARUBOZU'] < 0),
        (d['CDLSHOOTINGSTAR'] > 0),
        (d['CDLSHOOTINGSTAR'] < 0),
        ]
    r = 0
    m = 1
    #轉成10進制方便 Human-readable
    for i in range(len(l)):
        if l[i] : r += m
        m = m * 2
    return int(r)

def run_simulation(policy, prices, d):
    
    budget = (prices.loc[[0], ['close']].values[0]) * d.cash()
    num_stocks = 0
    share_value = 0
    p = pd.DataFrame(columns = ['total'])
    lastTurn = len(prices) - 1
    
    for i in range(lastTurn):
        closed  = prices.loc[[i], ['close']].values[0]
        openPrice  = prices.loc[[i + 1], ['open']].values[0]
        
        current_portfolio = budget + (num_stocks * share_value)
        bHolding = num_stocks
        action = policy.select_action(prices.loc[i])
        
        share_value = openPrice
        if action == 'Buy' and budget >= openPrice:
            budget -= share_value 
            num_stocks += 1
        elif action == 'Sell' and num_stocks > 0:
            budget += openPrice
            num_stocks -= 1
        else:
            action = 'Hold'

        p = p.append( {'total' : current_portfolio } , ignore_index=True)
        
        if not (i % 20):
            d.dOut('-----------------------')
            d.dOut('第%s日｜總資產：%s｜持股：%s｜市值%s' % (i, current_portfolio, bHolding, bHolding * closed))
            d.dOut('-----------------------')
        
        actionText = {'Buy': '買！', 'Sell':'沽！', 'Hold': '坐！'}
        day = prices.loc[[i], ['date']].values[0][0]
        outputText = '%s｜%s' % (day, actionText[action])
        d.dOut(outputText)
        
        if i == lastTurn:
            d.dOut('-----------------------')
            d.dOut('第%s日｜總資產：%s｜持股：%s｜市值%s' % (i, current_portfolio, bHolding, bHolding * closed))
            d.dOut('-----------------------')
            
    share_value = prices['close'].tail(1).values[0]
    portfolio = budget + num_stocks * share_value
    p = p.append( {'total' : portfolio } , ignore_index=True)
    return [portfolio, p]

def run_simulations(policy, prices, d, num = 1):
    final_portfolios = list()
    dh = pd.DataFrame()
    dh = pd.concat([dh, prices['date']], axis=1)
    for i in range(num):
        final_portfolio = run_simulation(policy, prices, d)
        final_portfolios.append(final_portfolio[0])
        df = prices.reset_index(drop=True)
        de = pd.concat([df, final_portfolio[1]['total']], axis=1)
        dh = pd.concat([dh, final_portfolio[1]['total']], axis=1)
        plt.grid(False)
        plt.axis('off')
        plt.plot(de['date'], (de['close'] / de['close'][0]), label = "Stock Price",  color="grey")
        plt.plot(de['date'], (de['total'] / de['total'][0]), label = "Bot Performance", color="green")
        plt.legend()
        plt.show() 
        de = de.set_index('date')
    if d.csvName() : dh.to_csv(d.csvName())
    avg, std = np.mean(final_portfolios), np.std(final_portfolios)
    return avg, std

def indicator(x, name):
    x = x.to_frame()
    x = x.rename({0:name}, axis='columns')
    return x

#計算技術指標
def get_prices(x):
    df = pd.read_csv(x)
    df = df.dropna()
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    
    sma5 = indicator(talib.MA(df['close'], 5), 'SMA_5')
    sma10 = indicator(talib.MA(df['close'], 10), 'SMA_10')
    sma50 = indicator(talib.MA(df['close'], 50), 'SMA_50')
    sma120 = indicator(talib.MA(df['close'], 120), 'SMA_120')
    rsi = indicator(talib.RSI(df['close']), 'RSI_14')
    sma5u = sma5.diff().rename(columns={'SMA_5':'SMA_5_u'})
    sma10u = sma10.diff().rename(columns={'SMA_10':'SMA_10_u'})
    sma50u = sma50.diff().rename(columns={'SMA_50':'SMA_50_u'})
    sma120u = sma120.diff().rename(columns={'SMA_120':'SMA_120_u'})
    
    CDL2CROWS = indicator(abstract.CDL2CROWS(df), 'CDL2CROWS')
    CDL3BLACKCROWS = indicator(abstract.CDL3BLACKCROWS(df), 'CDL3BLACKCROWS')
    CDL3INSIDE = indicator(abstract.CDL3INSIDE(df), 'CDL3INSIDE')
    CDL3LINESTRIKE = indicator(abstract.CDL3LINESTRIKE(df), 'CDL3LINESTRIKE')
    CDL3OUTSIDE = indicator(abstract.CDL3OUTSIDE(df), 'CDL3OUTSIDE')
    CDL3STARSINSOUTH = indicator(abstract.CDL3STARSINSOUTH(df), 'CDL3STARSINSOUTH')
    CDL3WHITESOLDIERS = indicator(abstract.CDL3WHITESOLDIERS(df), 'CDL3WHITESOLDIERS')
    CDLABANDONEDBABY = indicator(abstract.CDLABANDONEDBABY(df), 'CDLABANDONEDBABY')
    CDLADVANCEBLOCK = indicator(abstract.CDLADVANCEBLOCK(df), 'CDLADVANCEBLOCK')
    CDLBELTHOLD = indicator(abstract.CDLBELTHOLD(df), 'CDLBELTHOLD')
    CDLBREAKAWAY = indicator(abstract.CDLBREAKAWAY(df), 'CDLBREAKAWAY')
    CDLCLOSINGMARUBOZU = indicator(abstract.CDLCLOSINGMARUBOZU(df), 'CDLCLOSINGMARUBOZU')
    CDLCONCEALBABYSWALL = indicator(abstract.CDLCONCEALBABYSWALL(df), 'CDLCONCEALBABYSWALL')
    CDLCOUNTERATTACK = indicator(abstract.CDLCOUNTERATTACK(df), 'CDLCOUNTERATTACK')
    CDLDARKCLOUDCOVER = indicator(abstract.CDLDARKCLOUDCOVER(df), 'CDLDARKCLOUDCOVER')
    CDLDOJI = indicator(abstract.CDLDOJI(df), 'CDLDOJI')
    CDLDOJISTAR = indicator(abstract.CDLDOJISTAR(df), 'CDLDOJISTAR')
    CDLDRAGONFLYDOJI = indicator(abstract.CDLDRAGONFLYDOJI(df), 'CDLDRAGONFLYDOJI')
    CDLENGULFING = indicator(abstract.CDLENGULFING(df), 'CDLENGULFING')
    CDLEVENINGDOJISTAR = indicator(abstract.CDLEVENINGDOJISTAR(df), 'CDLEVENINGDOJISTAR')
    CDLEVENINGSTAR = indicator(abstract.CDLEVENINGSTAR(df), 'CDLEVENINGSTAR')
    CDLGAPSIDESIDEWHITE = indicator(abstract.CDLGAPSIDESIDEWHITE(df), 'CDLGAPSIDESIDEWHITE')
    CDLGRAVESTONEDOJI = indicator(abstract.CDLGRAVESTONEDOJI(df), 'CDLGRAVESTONEDOJI')
    CDLHAMMER = indicator(abstract.CDLHAMMER(df), 'CDLHAMMER')
    CDLHANGINGMAN = indicator(abstract.CDLHANGINGMAN(df), 'CDLHANGINGMAN')
    CDLHARAMI = indicator(abstract.CDLHARAMI(df), 'CDLHARAMI')
    CDLHARAMICROSS = indicator(abstract.CDLHARAMICROSS(df), 'CDLHARAMICROSS')
    CDLHIGHWAVE = indicator(abstract.CDLHIGHWAVE(df), 'CDLHIGHWAVE')
    CDLHIKKAKE = indicator(abstract.CDLHIKKAKE(df), 'CDLHIKKAKE')
    CDLHIKKAKEMOD = indicator(abstract.CDLHIKKAKEMOD(df), 'CDLHIKKAKEMOD')
    CDLHOMINGPIGEON = indicator(abstract.CDLHOMINGPIGEON(df), 'CDLHOMINGPIGEON')
    CDLIDENTICAL3CROWS = indicator(abstract.CDLIDENTICAL3CROWS(df), 'CDLIDENTICAL3CROWS')
    CDLINNECK = indicator(abstract.CDLINNECK(df), 'CDLINNECK')
    CDLINVERTEDHAMMER = indicator(abstract.CDLINVERTEDHAMMER(df), 'CDLINVERTEDHAMMER')
    CDLKICKING = indicator(abstract.CDLKICKING(df), 'CDLKICKING')
    CDLKICKINGBYLENGTH = indicator(abstract.CDLKICKINGBYLENGTH(df), 'CDLKICKINGBYLENGTH')
    CDLLADDERBOTTOM = indicator(abstract.CDLLADDERBOTTOM(df), 'CDLLADDERBOTTOM')
    CDLLONGLEGGEDDOJI = indicator(abstract.CDLLONGLEGGEDDOJI(df), 'CDLLONGLEGGEDDOJI')
    CDLLONGLINE = indicator(abstract.CDLLONGLINE(df), 'CDLLONGLINE')
    CDLMARUBOZU = indicator(abstract.CDLMARUBOZU(df), 'CDLMARUBOZU')
    CDLMATCHINGLOW = indicator(abstract.CDLMATCHINGLOW(df), 'CDLMATCHINGLOW')
    CDLMATHOLD = indicator(abstract.CDLMATHOLD(df), 'CDLMATHOLD')
    CDLMORNINGDOJISTAR = indicator(abstract.CDLMORNINGDOJISTAR(df), 'CDLMORNINGDOJISTAR')
    CDLMORNINGSTAR = indicator(abstract.CDLMORNINGSTAR(df), 'CDLMORNINGSTAR')
    CDLONNECK = indicator(abstract.CDLONNECK(df), 'CDLONNECK')
    CDLPIERCING = indicator(abstract.CDLPIERCING(df), 'CDLPIERCING')
    CDLRICKSHAWMAN = indicator(abstract.CDLRICKSHAWMAN(df), 'CDLRICKSHAWMAN')
    CDLRISEFALL3METHODS = indicator(abstract.CDLRISEFALL3METHODS(df), 'CDLRISEFALL3METHODS')
    CDLSEPARATINGLINES = indicator(abstract.CDLSEPARATINGLINES(df), 'CDLSEPARATINGLINES')
    CDLSHOOTINGSTAR = indicator(abstract.CDLSHOOTINGSTAR(df), 'CDLSHOOTINGSTAR')
    CDLSHORTLINE = indicator(abstract.CDLSHORTLINE(df), 'CDLSHORTLINE')
    CDLSPINNINGTOP = indicator(abstract.CDLSPINNINGTOP(df), 'CDLSPINNINGTOP')
    CDLSTALLEDPATTERN = indicator(abstract.CDLSTALLEDPATTERN(df), 'CDLSTALLEDPATTERN')
    CDLSTICKSANDWICH = indicator(abstract.CDLSTICKSANDWICH(df), 'CDLSTICKSANDWICH')
    CDLTAKURI = indicator(abstract.CDLTAKURI(df), 'CDLTAKURI')
    CDLTASUKIGAP = indicator(abstract.CDLTASUKIGAP(df), 'CDLTASUKIGAP')
    CDLTHRUSTING = indicator(abstract.CDLTHRUSTING(df), 'CDLTHRUSTING')
    CDLTRISTAR = indicator(abstract.CDLTRISTAR(df), 'CDLTRISTAR')
    CDLUNIQUE3RIVER = indicator(abstract.CDLUNIQUE3RIVER(df), 'CDLUNIQUE3RIVER')
    CDLUPSIDEGAP2CROWS = indicator(abstract.CDLUPSIDEGAP2CROWS(df), 'CDLUPSIDEGAP2CROWS')
    CDLXSIDEGAP3METHODS = indicator(abstract.CDLXSIDEGAP3METHODS(df), 'CDLXSIDEGAP3METHODS')
    
    macd, macdsignal, macdhist = talib.MACD(df['close'])
    macd = indicator(macd, 'macd')
    macdsignal = indicator(macdsignal, 'macdsignal')
    macdhist = indicator(macdhist, 'macdhist')
    
    macdhistu = macdhist.diff().rename(columns={'macdhist':'macdhist_u'})
    
    upper, middle, lower = talib.BBANDS(df['close'])
    upper = indicator(upper, 'upper')
    lower = indicator(lower, 'lower')


    df = pd.concat([df, sma5, sma5u, sma10, sma10u, sma50, sma50u, sma120, sma120u,  rsi, CDL2CROWS, CDL3BLACKCROWS,
    CDL3INSIDE, CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, CDL3WHITESOLDIERS, CDLABANDONEDBABY,
    CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,
    CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI,
    CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, 
    CDLINNECK, CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, 
    CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,
    CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,
    CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS, macd, macdsignal, macdhist, upper, lower,
    macdhistu], axis=1)
    
    df = df[(df['SMA_50'] > 0)]
    df = df.reset_index(drop=True)
    return df

def run(d, stock = False):
    actions = ['Buy', 'Sell', 'Hold']
    
    #選擇policy
    
    #policy = rsiPolicy(actions)
    #policy = macdPolicy(actions)
    policy = cheatingPolicy(actions)
    
    #不指定股票作按指標測試全部樣本
    if (stock == False):
        file = {
            'Apple' : 'aapl', 
            'Tesla' : 'tsla',
            'Disney' : 'dis',
            'Carnival' : 'ccl',
            'SQQQ' : 'sqqq',
            'Murphy Oil' : 'mur',
            'First Solar' : 'fslr',
            'Suncor Energy' : 'su',
            '港視' : '1137',
            '卓爾' : '2098',
            '數碼通' : '315',
            '港交所' : '388',
            '香港電訊' : '6823',
            '騰訊' : '700',
            '中聯通' : '762',
            '中海油' : '883',
            '中移動' : '941',
            }
        for k, i in file.items():
            path = 'h/%s.csv' % i
            prices = get_prices(path)
            
            d.dOut(k)
            
            avg, std = run_simulations(policy, prices, d)
            
            stockP = ((prices['close'].tail(1).values[0] - prices['close'].head(1).values[0]) / prices['close'].head(1).values[0]) * 100
            pStart = prices.loc[[0], ['close']].values[0] * d.cash()
            pP = ((avg - pStart) / pStart) * 100

            d.out('%s測試結果' %k)
            d.out('總資產：%s｜回報：%s%%｜期內股價表現：%s%%' % (avg, pP, stockP))
            d.out('-----------------------')
            
    #指定股票則製作隨機群組
    else:
        path = 'h/%s.csv' % stock
        prices = get_prices(path)
        policy = RandomDecisionPolicy(actions)
        avg, std = run_simulations(policy, prices, d, 100)
        
        stockP = ((prices['close'].tail(1).values[0] - prices['close'].head(1).values[0]) / prices['close'].head(1).values[0]) * 100
        pStart = prices.loc[[0], ['close']].values[0] * d.cash()
        pP = ((avg - pStart) / pStart) * 100
        
        d.out('-----------------------')
        d.out('100次測試結果')
        d.out('平均總資產：%s｜回報：%s%%｜期內股價表現：%s%%' % (avg, pP, stockP))
        d.out('-----------------------')

class n:
    def __init__(self):
        self.v = False
        self.t = open("report.txt", "w")
        self.d = False
        self.p = False
        self.startCash = 10
    def printToFile(self):
        self.v = True
    def detailOut(self):
        self.d = True
    def out(self, t):
        if self.v: 
            self.t.write(str(t))
            self.t.write('\n')
        else: print(t)
    def dOut(self, t):
        if not self.d : return True
        self.out(t)
    def __exit__(self):
        self.t.close()
    def setCsvName(self, p = False):
        if not self.p: self.p = "r/%sR.csv" % p
        else: return False
    def csvName(self):
        return self.p
    def cash(self):
        return self.startCash

if __name__ == '__main__':
    d = n()
    
    #儲存txt，不輸出console
    #d.printToFile()
    
    #詳細紀錄
    d.detailOut()
    
    #儲存詳細紀錄
    #d.setCsvName('report')
    
    #跑晒全部sample
    run(d)
    
    #指定sample跑隨機100次例子
    #run(d, 'tsla')


