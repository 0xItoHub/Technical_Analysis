import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 仮想通貨のシンボルを設定
symbol = "BTC-USD"  # Bitcoinの例

# データの期間を設定
start_date = "2023-01-01"
end_date = "2024-08-01"

# データを取得
data = yf.download(symbol, start=start_date, end=end_date)

# ボリンジャーバンドの計算
window = 20  # 移動平均期間
data['SMA'] = data['Close'].rolling(window=window).mean()
data['STD'] = data['Close'].rolling(window=window).std()
data['Upper Band'] = data['SMA'] + (data['STD'] * 2)
data['Lower Band'] = data['SMA'] - (data['STD'] * 2)

# チャートを描画
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Close Price', color='blue')
plt.plot(data.index, data['SMA'], label='20 Day SMA', color='orange')
plt.plot(data.index, data['Upper Band'], label='Upper Band', color='green')
plt.plot(data.index, data['Lower Band'], label='Lower Band', color='red')
plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='gray', alpha=0.2)
plt.title(f'{symbol} Price with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
