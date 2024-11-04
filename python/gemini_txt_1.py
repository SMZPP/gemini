import google.generativeai as genai
import os


# APIキーを設定 
genai.configure(api_key=os.environ["API_KEY"])

# Gemini API モデルを選択
model = genai.GenerativeModel("gemini-1.5-flash")

# APIを利用
user_input = input("知りたいことを聞いてください: ")
response = model.generate_content(user_input)
print(response.text)