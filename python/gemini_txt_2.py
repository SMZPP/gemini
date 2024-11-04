import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])

# ストリーミングでテキストを生成
# デフォルトでは、モデルはテキスト生成プロセス全体が完了した後にレスポンスを返します。
# 結果全体を待たずに、
# ストリーミングを使用して部分的な結果を処理することで、
# より高速なインタラクションを実現できます
model = genai.GenerativeModel("gemini-1.5-flash")
user_input = input("知りたいことを聞いてください: ")
response = model.generate_content(user_input, stream=True)

for chunk in response:
  print(chunk.text)
  print("_" * 80)
