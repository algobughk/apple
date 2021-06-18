# apple
蘋果專欄  

【一注到尾？逢高減？小注怡情？人工智能bot幫你搵策略】  
https://hk.appledaily.com/finance/20210517/YN4THAVLZRC5LDNEJKMMLEQQ6M/  

【股海忌死牛一面頸 AI都學識要轉策略】  
https://hk.appledaily.com/finance/20210524/LDIGR56GVRBDBB4AQXPRKXF7U4/  

【Python炒股bot實測近20股票 一個指標較亂買賺多倍】  
https://hk.appledaily.com/finance/20210531/Z5I7GO36PRF3TGIOPO2XTUVPF4/  

【用Tesla升跌情境trade港視 贏All in長坐多3成】  
https://hk.appledaily.com/finance/20210607/365QCI4KE5EGDJHMREFOWIYDJA/  

bot以python編寫，可下載免費軟件anaconda執行程式。資料夾h載有測試樣本歷史數據CSV檔案。圖片若選擇不在anaconda terminal展示而改作儲存，將會儲存於p資料夾，報告儲存在py檔資料夾的report.txt。  
anaconda：https://www.anaconda.com/  
bot下載：https://github.com/algobughk/apple  

bot請配合服用：  

bot數據使用Bloomberg 5年歷史數據，然持第51日交易生成50天線後，才開始模擬交易。  
bot每日讀取OHLC資料後作買賣決定，然後以翌日開市價成交。  
為方便模擬，每次交易只買賣1股。港股不理會手數，逐股交易，強逼症患者可自行改code。  
bot起動資金為第一日調整後收市價10倍，以兼顧因合股等原因，難以劃一固定金額，如5年前SQQQ 1股高達1,528美金，及調整後收市價只為24美元的Apple，及不同股票間的可比較性。  
股價數據為經派息、合股及拆股等處理後的調整後價格。  
Bot暫不考慮交易成本。  

AI bot (apple_ai.py)：  

AI採用Q-network形式強化學習（reinforcement learning）  
bot沒採用常用的Bellman方程更新Q-table，因測試中效果很差  
bot會為每個action計算50日後股價變化影響  
獎勵機制中有機會成本，減少bot出現「取勝唯一法︰『及早離去』四字而矣。」情況。不過，當股價下跌時，機會成本則變負，即獎勵持有現金。  
程式有貪婪系數（greedy），放大持貨追貨的獎勵，能提升處理爆升股的表現，不過亦令處理下跌股的表現有所下降。  
bot最初會隨機作決定，以模索不同選擇的後果，並隨訓練次數提升，減少隨機決定，default設定是處理1萬交易日後就完全透過Q-table決策，以每回合1,200步計，即略多於8回合。  
bot買賣決定是隨機，不作股價走勢預測，只學習持股最佳倉位。  
若AI覺得現時倉位已是較佳解，則會透過買/賣0股拒絕執行，  

關於熱量圖：  
熱量圖垂直的 Y 軸代表電腦作決定時的持倉水平，每格一成，第一格代表10%持倉以下，第二格代表10%至20%持倉。  
橫向的 X 軸代表改變去到哪水平持倉，同樣是每格一成。當XY相同。  
譬如X1Y1、X2Y2、X3Y3……代表持倉不變，而這些方格左面代表沽貨到該水平（的獎勵，以顏色代表），右面則是增持到該水平（的獎勵，以顏色代表）。  

普通bot (apple_backtest.py)：

主要為回測工具，根據指定policy硬性執行交易。  
預設數個規則，可供選擇，其中一個為隨機決定。  
預載多項技術指標，如平均線、MACD、保加力通道及陰陽燭組合。  

測試股票樣本：  
美股：Apple、Tesla、迪士尼、嘉年華集團、SQQQ、墨菲石油、第一太陽能及森科能源。  
港股：港視（1137）、卓爾（2098）、數碼通（315）、港交所（388）、香港電訊（6823）、騰訊（700）、中聯通（762）、中海油（883）及中移動（941）  
