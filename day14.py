import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. .envファイルから秘密のキーを読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Geminiの設定
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. AIにメッセージを送る
print("AIに接続中...")
response = model.generate_content("Pythonを勉強中の私に、一言励ましの言葉をください。")

# 4. 返事を表示
print("-" * 30)
print(response.text)
print("-" * 30)