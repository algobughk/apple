# -*- coding: utf-8 -*-

import pandas as pd
import talib
from talib import abstract

def indicator(x, name):
    x = x.to_frame()
    x = x.rename({0:name}, axis='columns')
    return x

def get_prices(x):
    df = pd.read_csv('h/%s.csv' % x)
    df = df.dropna()
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    
    #生成技術指標
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

    df = pd.concat([df, sma5, sma5u, sma10, sma10u, sma50, sma50u, sma120, sma120u,  rsi, CDL2CROWS, CDL3BLACKCROWS,
    CDL3INSIDE, CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, CDL3WHITESOLDIERS, CDLABANDONEDBABY,
    CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,
    CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI,
    CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, 
    CDLINNECK, CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, 
    CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,
    CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,
    CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS, macd, macdsignal, macdhist 
    ], axis=1)
    
    df = df[(df['SMA_50'] > 0)]
    df = df.reset_index(drop=True)
    return df

def flagGen(d):
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
        ]
    r = 0
    m = 1
    for i in range(len(l)):
        if l[i] : r += m
        m = m * 2
    return int(r)

def flag(x):
    n = [
        '現價高過5日線',
        '5日線高過10日線', 
        '10日線高過50日線', 
        'RSI高過80',
        'RSI低過20',
        '5日線升',
        '10日線升',
        '50日線升',
        'macdhist正數',
         ]
    l = [int(d) for d in str(bin(x))[2:]][::-1]
    txt = []
    for i in range(len(l)):
        if l[i] == 1: txt.append(n[i])
    return txt

def getPo(t):
    x = t['close_x']
    y = t['close_y']
    if x == 0 or y == 0: return 0
    elif x > y : return x / y
    else: return y / x

#分析的股票
h = get_prices('tsla')
df = pd.DataFrame(columns=['state', 'change'])
#加入10日後10日線作比較
h['10day'] = h['SMA_10'].shift(-10)
#移除最後無比較的10日
h = h[:-10]
#計算狀態
h['state'] = h.apply(lambda x: flagGen(x),axis=1)
#清走不用的資料
h = h[['close', '10day', 'state']]
#分開及計算升跌日子
h_p = h[(h['10day'] > h['close'])].groupby('state', as_index=False, sort=False).count()[['state', 'close']]
h_n = h[(h['close'] > h['10day'])].groupby('state', as_index=False, sort=False).count()[['state', 'close']]
f = pd.merge(h_p, h_n, on=['state'])[['state','close_x', 'close_y']]
f.set_index("state", inplace = True)
f.sort_index()

#刪走樣本太少的例子
f['sum'] = f['close_x'] + f['close_y']
f = f[(f['sum'] > 30)]

f_p = f[(f['close_x'] > f['close_y'])]
f_n = f[(f['close_y'] > f['close_x'])]

print('\n升勢情境：%s' % f_p.index)
print('跌勢情境：%s' % f_n.index)

#由編號查詢組合方法:
#flag(1234)
