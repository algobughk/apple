# -*- coding: utf-8 -*-

import pandas as pd
import talib
from talib import abstract
import random
import time

#人口
population = 300

#培育至第幾代
generations = 50

#每人帶多少基因
gene_num = 10

#17個股票樣本
stock_li = [
    '315', '388', '700', '762', '883', '941', '1137', '2098', '6823', 'aapl', 'ccl', 'dis', 'fslr', 'mur', 'sqqq','tsla', 'su'
     ]

def indicator(x, name):
    x = x.to_frame()
    x = x.rename({0:name}, axis='columns')
    return x

def gen_ta(path):
    df = pd.read_csv('h/%s.csv' % path)
    df = df.dropna()
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    
    #生成技術指標
    sma5 = indicator(talib.MA(df['close'], 5), 'SMA_5')
    sma10 = indicator(talib.MA(df['close'], 10), 'SMA_10')
    sma50 = indicator(talib.MA(df['close'], 50), 'SMA_50')
    rsi = indicator(talib.RSI(df['close']), 'RSI_14')
    sma5u = sma5.diff().rename(columns={'SMA_5':'SMA_5_u'})
    sma10u = sma10.diff().rename(columns={'SMA_10':'SMA_10_u'})
    sma50u = sma50.diff().rename(columns={'SMA_50':'SMA_50_u'})
    
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

    df = pd.concat([df, sma5, sma5u, sma10, sma10u, sma50, sma50u,  rsi, CDL2CROWS, CDL3BLACKCROWS,
    CDL3INSIDE, CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, CDL3WHITESOLDIERS, CDLABANDONEDBABY,
    CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,
    CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI,
    CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, 
    CDLINNECK, CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, 
    CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,
    CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,
    CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS, macd, macdsignal, macdhist 
    ], axis=1)
    
    df['next_open'] = df['open'].shift(-1)
    df = df[:-1]
    
    df = df[(df['SMA_50'] > 0)]
    df = df.reset_index(drop=True)
    
    return df

#生成技術指標
stock_ta_li = {}
for i in stock_li:
    stock_ta_li[i] = gen_ta(i)

#「基因」
def macd(df):
    if df['macdhist'] > 0: return 1
    else: return -1
    
def rsi(df):
    if df['RSI_14'] < 30: return 1
    elif df['RSI_14'] > 70 : return -1
    return 0

def sma5up(df):
    if df['SMA_5_u'] > 0: return 1
    else: return -1
    
def sma10up(df):
    if df['SMA_10_u'] > 0: return 1
    else: return -1
    
def sma50up(df):
    if df['SMA_50_u'] > 0: return 1
    else: return -1
    
def close_qt_sma_5(df):
    if df['close'] > df['SMA_5']:return 1
    else: return -1
    
def close_lt_sma_5(df):
    if df['close'] < df['SMA_5']:return 1
    else: return -1

def sma10_gt_50(df):
    if df['SMA_10'] > df['SMA_50']:return 1
    else: return -1
    
def sma10_lt_50(df):
    if df['SMA_10'] < df['SMA_50']:return 1
    else: return -1
    
def close_qt_sma_10(df):
    if df['close'] > df['SMA_10']:return 1
    else: return -1
    
def close_lt_sma_10(df):
    if df['close'] < df['SMA_10']:return 1
    else: return -1
    
def close_qt_sma_50(df):
    if df['close'] > df['SMA_50']:return 1
    else: return -1
    
def close_lt_sma_50(df):
    if df['close'] < df['SMA_50']:return 1
    else: return -1
    
def sma5_gt_10(df):
    if df['SMA_5'] > df['SMA_10']:return 1
    else: return -1
    
def sma5_lt_10(df):
    if df['SMA_5'] < df['SMA_10']:return 1
    else: return -1
    
def sma5_gt_50(df):
    if df['SMA_5'] > df['SMA_50']:return 1
    else: return -1
    
def sma5_lt_50(df):
    if df['SMA_5'] < df['SMA_50']:return 1
    else: return -1
    
def CDL2CROWS(df):
    if df['CDL2CROWS'] > 1: return 1
    elif df['CDL2CROWS'] < -1: return -1
    return 0

def CDL3BLACKCROWS(df):
    if df['CDL3BLACKCROWS'] > 1: return 1
    elif df['CDL3BLACKCROWS'] < -1: return -1
    return 0

def CDL3INSIDE(df):
    if df['CDL3INSIDE'] > 1: return 1
    elif df['CDL3INSIDE'] < -1: return -1
    return 0

def CDL3LINESTRIKE(df):
    if df['CDL3LINESTRIKE'] > 1: return 1
    elif df['CDL3LINESTRIKE'] < -1: return -1
    return 0
    
def CDL3OUTSIDE(df):
    if df['CDL3OUTSIDE'] > 1: return 1
    elif df['CDL3OUTSIDE'] < -1: return -1
    return 0

def CDL3STARSINSOUTH(df):
    if df['CDL3STARSINSOUTH'] > 1: return 1
    elif df['CDL3STARSINSOUTH'] < -1: return -1
    return 0

def CDL3WHITESOLDIERS(df):
    if df['CDL3WHITESOLDIERS'] > 1: return 1
    elif df['CDL3WHITESOLDIERS'] < -1: return -1
    return 0

def CDLABANDONEDBABY(df):
    if df['CDLABANDONEDBABY'] > 1: return 1
    elif df['CDLABANDONEDBABY'] < -1: return -1
    return 0

def CDLADVANCEBLOCK(df):
    if df["CDLADVANCEBLOCK"] > 1: return 1
    elif df["CDLADVANCEBLOCK"] < -1: return -1
    return 0
def CDLBELTHOLD(df):
    if df["CDLBELTHOLD"] > 1: return 1
    elif df["CDLBELTHOLD"] < -1: return -1
    return 0
def CDLBREAKAWAY(df):
    if df["CDLBREAKAWAY"] > 1: return 1
    elif df["CDLBREAKAWAY"] < -1: return -1
    return 0
def CDLCLOSINGMARUBOZU(df):
    if df["CDLCLOSINGMARUBOZU"] > 1: return 1
    elif df["CDLCLOSINGMARUBOZU"] < -1: return -1
    return 0
def CDLCONCEALBABYSWALL(df):
    if df["CDLCONCEALBABYSWALL"] > 1: return 1
    elif df["CDLCONCEALBABYSWALL"] < -1 : return -1
    return 0
def CDLCOUNTERATTACK(df):
    if df["CDLCOUNTERATTACK"] > 1: return 1
    elif df["CDLCOUNTERATTACK"] < -1: return -1
    return 0
def CDLDARKCLOUDCOVER(df):
    if df["CDLDARKCLOUDCOVER"] > 1: return 1
    elif df["CDLDARKCLOUDCOVER"] < -1: return -1
    return 0
def CDLDOJI(df):
    if df["CDLDOJI"] > 1: return 1
    elif df["CDLDOJI"] < -1: return -1
    return 0
def CDLDOJISTAR(df):
    if df["CDLDOJISTAR"] > 1: return 1
    elif df["CDLDOJISTAR"] < -1: return -1
    return 0
def CDLDRAGONFLYDOJI(df):
    if df["CDLDRAGONFLYDOJI"] > 1: return 1
    elif df["CDLDRAGONFLYDOJI"] < -1: return -1
    return 0
def CDLENGULFING(df):
    if df["CDLENGULFING"] > 1: return 1
    elif df["CDLENGULFING"] < -1: return -1
    return 0
def CDLEVENINGDOJISTAR(df):
    if df["CDLEVENINGDOJISTAR"] > 1: return 1
    elif df["CDLEVENINGDOJISTAR"] < -1: return -1
    return 0
def CDLEVENINGSTAR(df):
    if df["CDLEVENINGSTAR"] > 1: return 1
    elif df["CDLEVENINGSTAR"] < -1: return -1
    return 0
def CDLGAPSIDESIDEWHITE(df):
    if df["CDLGAPSIDESIDEWHITE"] > 1: return 1
    elif df["CDLGAPSIDESIDEWHITE"] < -1: return -1
    return 0
def CDLGRAVESTONEDOJI(df):
    if df["CDLGRAVESTONEDOJI"] > 1: return 1
    elif df["CDLGRAVESTONEDOJI"] < -1: return -1
    return 0
def CDLHAMMER(df):
    if df["CDLHAMMER"] > 1: return 1
    elif df["CDLHAMMER"] < -1: return -1
    return 0
def CDLHANGINGMAN(df):
    if df["CDLHANGINGMAN"] > 1: return 1
    elif df["CDLHANGINGMAN"] < -1: return -1
    return 0
def CDLHARAMI(df):
    if df["CDLHARAMI"] > 1: return 1
    elif df["CDLHARAMI"] < -1: return -1
    return 0
def CDLHARAMICROSS(df):
    if df["CDLHARAMICROSS"] > 1: return 1
    elif df["CDLHARAMICROSS"] < -1: return -1
    return 0
def CDLHIGHWAVE(df):
    if df["CDLHIGHWAVE"] > 1: return 1
    elif df["CDLHIGHWAVE"] < -1 : return -1
    return 0
def CDLHIKKAKE(df):
    if df["CDLHIKKAKE"] > 1: return 1
    elif df["CDLHIKKAKE"] <-1: return -1
    return 0
def CDLHIKKAKEMOD(df):
    if df["CDLHIKKAKEMOD"] > 1: return 1
    elif df["CDLHIKKAKEMOD"] < -1 : return -1
    return 0
def CDLHOMINGPIGEON(df):
    if df["CDLHOMINGPIGEON"] > 1: return 1
    elif df["CDLHOMINGPIGEON"] < -1: return -1
    return 0
def CDLIDENTICAL3CROWS(df):
    if df["CDLIDENTICAL3CROWS"] > 1: return 1
    elif df["CDLIDENTICAL3CROWS"] < -1: return -1
    return 0
def CDLINNECK(df):
    if df["CDLINNECK"] > 1: return 1
    elif df["CDLINNECK"] < -1: return -1
    return 0
def CDLINVERTEDHAMMER(df):
    if df["CDLINVERTEDHAMMER"] > 1: return 1
    elif df["CDLINVERTEDHAMMER"] < -1: return -1
    return 0
def CDLKICKING(df):
    if df["CDLKICKING"] > 1: return 1
    elif df["CDLKICKING"] < -1: return -1
    return 0
def CDLKICKINGBYLENGTH(df):
    if df["CDLKICKINGBYLENGTH"] > 1: return 1
    elif df["CDLKICKINGBYLENGTH"] < -1: return -1
    return 0
def CDLLADDERBOTTOM(df):
    if df["CDLLADDERBOTTOM"] > 1: return 1
    elif df["CDLLADDERBOTTOM"] < -1: return -1
    return 0
def CDLLONGLEGGEDDOJI(df):
    if df["CDLLONGLEGGEDDOJI"] > 1: return 1
    elif df["CDLLONGLEGGEDDOJI"] < -1: return -1
    return 0
def CDLLONGLINE(df):
    if df["CDLLONGLINE"] > 1: return 1
    elif df["CDLLONGLINE"] < -1: return -1
    return 0
def CDLMARUBOZU(df):
    if df["CDLMARUBOZU"] > 1: return 1
    elif df["CDLMARUBOZU"] < -1: return -1
    return 0
def CDLMATCHINGLOW(df):
    if df["CDLMATCHINGLOW"] > 1: return 1
    elif df["CDLMATCHINGLOW"] < -1: return -1
    return 0

def CDLMATHOLD(df):
    if df["CDLMATHOLD"] > 1: return 1
    elif df["CDLMATHOLD"] < -1: return -1
    return 0

def CDLMORNINGDOJISTAR(df):
    if df["CDLMORNINGDOJISTAR"] > 1: return 1
    elif df["CDLMORNINGDOJISTAR"] < -1: return -1
    return 0

def CDLMORNINGSTAR(df):
    if df["CDLMORNINGSTAR"] > 1: return 1
    elif df["CDLMORNINGSTAR"] < -1: return -1
    return 0

def CDLONNECK(df):
    if df["CDLONNECK"] > 1: return 1
    elif df["CDLONNECK"] < -1: return -1
    return 0

def CDLPIERCING(df):
    if df["CDLPIERCING"] > 1: return 1
    elif df["CDLPIERCING"] < -1: return -1
    return 0

def CDLRICKSHAWMAN(df):
    if df["CDLRICKSHAWMAN"] > 1: return 1
    elif df["CDLRICKSHAWMAN"] < -1: return -1
    return 0

def CDLRISEFALL3METHODS(df):
    if df["CDLRISEFALL3METHODS"] > 1: return 1
    elif df["CDLRISEFALL3METHODS"] < -1: return -1
    return 0

def CDLSEPARATINGLINES(df):
    if df["CDLSEPARATINGLINES"] > 1: return 1
    elif df["CDLSEPARATINGLINES"] < -1: return -1
    return 0

def CDLSHOOTINGSTAR(df):
    if df["CDLSHOOTINGSTAR"] > 1: return 1
    elif df["CDLSHOOTINGSTAR"] < -1: return -1
    return 0

def CDLSHORTLINE(df):
    if df["CDLSHORTLINE"] > 1: return 1
    elif df["CDLSHORTLINE"] < -1: return -1
    return 0

def CDLSPINNINGTOP(df):
    if df["CDLSPINNINGTOP"] > 1: return 1
    elif df["CDLSPINNINGTOP"] < -1: return -1
    return 0

def CDLSTALLEDPATTERN(df):
    if df["CDLSTALLEDPATTERN"] > 1: return 1
    elif df["CDLSTALLEDPATTERN"] < -1: return -1
    return 0

def CDLSTICKSANDWICH(df):
    if df["CDLSTICKSANDWICH"] > 1: return 1
    elif df["CDLSTICKSANDWICH"] < -1: return -1
    return 0

def CDLTAKURI(df):
    if df["CDLTAKURI"] > 1: return 1
    elif df["CDLTAKURI"] < -1: return -1
    return 0

def CDLTASUKIGAP(df):
    if df["CDLTASUKIGAP"] > 1: return 1
    elif df["CDLTASUKIGAP"] < -1: return -1
    return 0

def CDLTHRUSTING(df):
    if df["CDLTHRUSTING"] > 1: return 1
    elif df["CDLTHRUSTING"] < -1: return -1
    return 0

def CDLTRISTAR(df):
    if df["CDLTRISTAR"] > 1: return 1
    elif df["CDLTRISTAR"] < -1: return -1
    return 0

def CDLUNIQUE3RIVER(df):
    if df["CDLUNIQUE3RIVER"] > 1: return 1
    elif df["CDLUNIQUE3RIVER"] < -1: return -1
    return 0

def CDLUPSIDEGAP2CROWS(df):
    if df["CDLUPSIDEGAP2CROWS"] > 1: return 1
    elif df["CDLUPSIDEGAP2CROWS"] < -1: return -1
    return 0

def CDLXSIDEGAP3METHODS(df):
    if df["CDLXSIDEGAP3METHODS"] > 1: return 1
    elif df["CDLXSIDEGAP3METHODS"] < -1 : return -1
    return 0

gene = (macd, rsi, sma5up, close_qt_sma_5, close_lt_sma_5, 
        close_qt_sma_10, close_lt_sma_10, close_qt_sma_50, 
        close_lt_sma_50, sma5_gt_10, sma5_lt_10, sma5_gt_50,
        sma5_lt_50, sma10up, sma10_gt_50, sma50up,
        sma10_lt_50, CDL2CROWS, CDL3BLACKCROWS, CDL3INSIDE,
        CDL3LINESTRIKE, CDL3OUTSIDE, CDL3STARSINSOUTH, CDL3WHITESOLDIERS,
        CDLABANDONEDBABY, CDLADVANCEBLOCK, CDLBELTHOLD, CDLBREAKAWAY, CDLCLOSINGMARUBOZU, CDLCONCEALBABYSWALL, CDLCOUNTERATTACK, CDLDARKCLOUDCOVER,
    CDLDOJI, CDLDOJISTAR, CDLDRAGONFLYDOJI, CDLENGULFING, CDLEVENINGDOJISTAR, CDLEVENINGSTAR, CDLGAPSIDESIDEWHITE, CDLGRAVESTONEDOJI,
    CDLHAMMER, CDLHANGINGMAN, CDLHARAMI, CDLHARAMICROSS, CDLHIGHWAVE, CDLHIKKAKE, CDLHIKKAKEMOD, CDLHOMINGPIGEON, CDLIDENTICAL3CROWS, 
    CDLINNECK, CDLINVERTEDHAMMER, CDLKICKING, CDLKICKINGBYLENGTH, CDLLADDERBOTTOM, CDLLONGLEGGEDDOJI, CDLLONGLINE, CDLMARUBOZU, 
    CDLMATCHINGLOW, CDLMATHOLD, CDLMORNINGDOJISTAR, CDLMORNINGSTAR, CDLONNECK, CDLPIERCING, CDLRICKSHAWMAN, CDLRISEFALL3METHODS,
    CDLSEPARATINGLINES, CDLSHOOTINGSTAR, CDLSHORTLINE, CDLSPINNINGTOP, CDLSTALLEDPATTERN, CDLSTICKSANDWICH, CDLTAKURI,
    CDLTASUKIGAP, CDLTHRUSTING, CDLTRISTAR, CDLUNIQUE3RIVER, CDLUPSIDEGAP2CROWS, CDLXSIDEGAP3METHODS)

#返回買賣決定
def trade(x , gene, geneList):
    count = 0
    for f in gene['dna']:
        count += geneList[f](x)
    if count > 0: return x['next_open'] * -1
    elif (count * -1) > 0: return x['next_open']
    return 0

#計算成績
def decision(dna, stock_ta_li, gene, cache):
    
    #檢查快取
    dna_txt = "_".join(str(v) for v in dna['dna'])
    if dna_txt in cache:
        return cache[dna_txt]
    
    #無快取則跑樣本
    gain = 0
    for stock in stock_ta_li:
        stock_ta_li[stock]['bhs'] = stock_ta_li[stock].apply(lambda x: trade(x, dna, gene), axis=1)
        bought = len(stock_ta_li[stock][(stock_ta_li[stock]['bhs'] < 0)])
        sold = len(stock_ta_li[stock][(stock_ta_li[stock]['bhs'] > 0)])
        gain += (stock_ta_li[stock]['bhs'].sum() / stock_ta_li[stock].at[(len(stock_ta_li[stock]) -1 ), 'close']) + bought - sold
        
    return gain

#交換基因
def reproduction(df, gene):
    pick = []
    #有相同則直接取用
    inner = list(set(df[0]) & set(df[1]))
    #僅一方有的基因
    outer = list(set(df[0]) ^ set(df[1]))
    if not len(inner)  == gene:
        pick = random.sample(range(len(outer)), gene - len(inner))
        for i in pick:
            inner.append(outer[i])
    return inner

#圖片參數list
mean = []
median = []
human_max =[] 

cache = {}

human = pd.DataFrame(columns = ['dna'])

print('開始')

#第一代隨機人仔
for p in range(population):
    dna = sorted(random.sample(range((len(gene) -1)), gene_num))
    human = human.append({'dna' : dna}, ignore_index=True)
    
print('創造咗%s隻人仔' % len(human))

for generation in range(generations):
    start_time = int(time.time())
    if generation == 0: print('In the beginning you created the wealth and the earth.')
    
    #交易
    human['gain'] = human.apply(lambda x: decision(x, stock_ta_li, gene, cache), axis=1)
    human['dna'] = human.dna.sort_values().apply(lambda x: sorted(x))
    
    #儲存快取
    for i in range(len(human)):
        cache["_".join(str(v) for v in human.at[i, 'dna'])] = human.at[i, 'gain']
    
    print('第%s代完成，運算耗時%s秒' % ((generation + 1), (int(time.time() - start_time))))
    print('平均： %s | 中位數： %s | 最高： %s' % (int(human['gain'].mean()),
           int(human['gain'].median()), int(human['gain'].max())))
    
    mean.append(human['gain'].mean())
    median.append(human['gain'].median())
    human_max.append(human['gain'].max())
    
    #開始配對
    human = human.sort_values(by=['gain'], ascending=False)[: int((population / 10) * -1)].reset_index(drop=True)['dna']
    top10 = human[:int(population / 10)]
    top10 = pd.concat([top10, human.sample(frac=1).reset_index(drop=True)[:len(top10)]], axis=1)
    human = pd.concat([human, human.sample(frac=1).reset_index(drop=True)], axis=1)
    human = pd.concat([top10, human]).reset_index(drop=True)
    
    #交換基因
    human['child'] = human.apply(lambda x: reproduction(x, gene_num), axis=1)
    
    #取代上一代
    human = human['child']
    human = human.to_frame(name="dna")
    

#總結成績 - 輸出到console
print('已檢查%s個組合' % len(cache))
top10 = human[:int(population / 10)]
for i in range(len(top10)):
    print('---------第%s名基因---------' % (i + 1))
    top10.at[i, 'dna'].sort()
    for dna in top10.at[i, 'dna']:
        
        print(gene[dna].__name__)
    print('')
        
record = pd.DataFrame([mean, median, human_max])
record.T.rename(columns={0: "mean", 1: "median", 2: 'max'}).plot()