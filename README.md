
# 仮想通貨ボリンジャーバンド可視化

このプロジェクトでは、`yfinance`ライブラリを使用して仮想通貨（この例ではビットコイン）の価格データを取得し、`matplotlib`でボリンジャーバンドを表示する可視化を行います。

## 概要

スクリプトは指定された仮想通貨の履歴価格データをYahoo Financeから取得し、単純移動平均（SMA）とボリンジャーバンドを計算してデータをプロットします。ボリンジャーバンドは、市場のボラティリティと価格の潜在的なレベルを測定するために使用されます。

## 特徴

- **仮想通貨価格取得**: 指定された仮想通貨の履歴価格データを取得します。
- **ボリンジャーバンド計算**: 指定された移動平均期間に基づいて上下のバンドを計算します。
- **データの可視化**: 価格データとボリンジャーバンドをプロットして視覚的に分析します。

## インストール

1. **リポジトリをクローン**:

   git clone https://github.com/yourusername/crypto-bollinger-bands.git
   cd crypto-bollinger-bands
   ```

2. **依存関係のインストール**:

   Pythonとpipがインストールされていることを確認し、以下のコマンドを実行してください。

   pip install yfinance matplotlib pandas

## 使用方法

1. **スクリプトの実行**:

   必要に応じてスクリプトを修正し（例: 仮想通貨のシンボルや日付範囲の変更）、以下のコマンドを実行します。

   python plot_crypto.py

2. **パラメータ**:

   - `symbol`: 仮想通貨のティッカーシンボル（例: ビットコインの場合は "BTC-USD"）。
   - `start_date`: 履歴データを取得する開始日（形式: YYYY-MM-DD）。
   - `end_date`: 履歴データを取得する終了日（形式: YYYY-MM-DD）。
   - `window`: 移動平均の期間（デフォルトは20日）。

## 出力例

![Figure_1](https://github.com/user-attachments/assets/4255261d-11ec-4702-8290-a89f03edb597)


*例: ビットコインの価格と20日ボリンジャーバンド。*

## 依存関係

- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。

## コントリビューション

コントリビューションは歓迎します！プルリクエストを送信する前に、[CONTRIBUTING](CONTRIBUTING.md)ガイドラインをお読みください。

