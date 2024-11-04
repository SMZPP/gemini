### 環境準備
* 前提
  * Pythonインストール済み

1. 下記のコマンドでGemini API SDKをインストールする
   ```
   pip install -q -U google-generativeai
   ```

1. Gemini APIキーを設定する
  1. [APIキー取得リンク](https://aistudio.google.com/app/apikey?hl=ja)でAPIキーを取得する
     * 必要なもの
       * Googleアカウント
     * 注意事項
       * API キーを共有したり公開コードに埋め込んだりしないでください
  
  1. 下記コマンドでAPIキーを設定する
      ```
      export API_KEY=<YOUR_API_KEY>
      ```
      ※`<YOUR_API_KEY>`を生成されたAPIキーを置換する
