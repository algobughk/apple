# -*- coding: utf-8 -*-

import pandas as pd
import talib
from talib import abstract

def indicator(x, name):
    x = x.to_frame()
    x = x.rename({0:name}, axis='columns')
    return x

def getPo(t):
    x = t['close_x']
    y = t['close_y']
    if x == 0 or y == 0: return 0
    elif x > y : return x / y
    else: return y / x

def get_prices(x):
    df = pd.read_csv('h/%s.csv' % x)
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
    CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS, macd, macdsignal, macdhist,
    upper, lower, macdhistu
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
    for i in range(len(l)):
        if l[i] : r += m
        m = m * 2
    return int(r)


def flag(x):
    if x == 0: return '表內均非' 
    n = [
        '現價高過5日線',
        '5日線高過10日線',  
        '10日線高過50日線', 
        'RSI高過80',
        'RSI低過20',
        '5日線升',
        '10日線升',
        '50日線升',
        'MACD柱正數',
        'MACD柱向上',
        '現價高過保力加通道頂',
        '現價低過保力加通道頂',
        '底部棄嬰 - 牛',
        '底部棄嬰 - 熊',
        '大敵當前 - 牛',
        '大敵當前 - 熊',
        '收市無影線 - 牛',
        '收市無影線 - 熊',
        '射擊之星 - 牛',
        '射擊之星 - 熊',
         ]
    l = [int(d) for d in str(bin(x))[2:]][::-1]
    txt = []
    for i in range(len(l)):
        if l[i] == 1: txt.append(n[i])
    return txt

def gotStock(x):
    h = get_prices(x)
    
    #加入10日後10日線作比較
    h['10day'] = h['SMA_10'].shift(-10)
    h = h[:-10]
    h['state'] = h.apply(lambda x: flagGen(x),axis=1)
    h['diff'] = h['SMA_10'] - h['10day']
    return h[['close', 'state', 'diff']]

#分析list
l = ['315', '388', '700', '762', '883', '941', '1137', '2098', '6823', 
     'aapl', 'ccl', 'dis', 'fslr', 'mur', 'sqqq', 'tsla', 'su']

df = pd.DataFrame()

print('started')

for i in range(len(l)):
    h2 = gotStock(l[i])
    #移除升跌幅不明顯的日子
    h2['diffP'] = h2['diff'] / h2['close']
    th = h2['diffP'].abs().mean()
    h2 = h2[((h2['diffP'] > th) | (h2['diffP']  < (th * -1)))]
    
    h3 = h2.groupby('state', as_index=False, sort=False)['close'].count()
    h_p = h2[h2['diff'] > 0].groupby('state', as_index=False, sort=False).count()
    h_n = h2[h2['diff'] < 0].groupby('state', as_index=False, sort=False).count()
    f = pd.merge(h_p, h_n, on=['state'])[['state','close_x', 'close_y']]
    f.set_index("state", inplace = True)
    f.sort_index()
    df = df.add(f, fill_value=0)

#移除出現次數太少的組合    
df['sum'] = df['close_x'] + df['close_y']
df = df[(df['sum'] > df['sum'].mean())]
df = df.sort_values(by=['sum'], ascending = False)

#移除升跌比例不明顯的組合
df['p'] = df.apply(lambda x: getPo(x),axis=1)
df = df[((df['p'] > df['p'].mean()) & (df['p'] > 2))]

print('清單')
print(df)

#p為比例
df_p = df[(df['close_x'] > df['close_y'])]
df_n = df[(df['close_y'] > df['close_x'])]

print('\n升勢情境：%s' % df_p.index)
print('升勢情境：%s' % df_n.index)

#由編號查詢組合方法:
#flag(1234)
