# debug.py
import os 
from dotenv import load_dotenv
import google.generativeai as genai

# .envを読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("--- デバッグ開始 ---")

# 1. APIキーのチェック
if not api_key:
    print("APIキーが読み込めてない")
    print(".envファイルがない、中身が空、ファイル名が違う")
else:
    # キーの最初の五文字だけを表示して確認 (全部は表示しない)
    print(f"APIキー読み込み成功: {api_key[:5]}********")

    # 2. モデル一覧の取得を試みる
    try:
        genai.configure(api_key=api_key)
        print("利用可能なモデルを探しています")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - 発見: {m.name}")
    except Exception as e:
        print(f"モデル一覧の取得に失敗しました: {e}")

print("--- デバッグ終了 ---")