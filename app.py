import streamlit as st
import os 
import google.generativeai as genai
from dotenv import load_dotenv

# 1. "金庫"の中に 'chat_history' がまだなければ、空のリストを作って入れる
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# 2. 今までの会話を画面に表示する (再実行されるたびにここが走る)
for message in st.session_state['chat_history']:
    st.write(message)

# 1. 環境変数の読み込み
# これがないとAPIキーが読み込めずエラーになります
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# キーが正しく読み込めているかチェック (本番では消すべきですが、デバック用に)
if not api_key:
    st.error("APIキーが見つかりません。 .envファイルを確認してください。")
else:
    # 2. Gemini APIの設定
    genai.configure(api_key=api_key)
    # モデルの準備 (gemini-2.5-flash は高速で安価なのでテストに最適です)
    # 役割を与える
    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction="あなたは熱血なPythonプログラミングのコーチです。ユーザーは初心者です。松岡修造のように熱く、ポジティブに、そして具体的にコードのアドバイスをしてください。語尾は「だ！」「できるぞ！」を使ってください。"
    )

    st.title("🤖 My First AI Bot")
    st.write("PFNへの道 Day 17: AIとWebアプリの連携")

    # 3. ユーザー入力エリア
    user_input = st.text_input("質問を入力してください", placeholder="例: Pythonの勉強法を教えて")

    # 4. 送信ボタンと処理
    if st.button("送信"):
        if user_input:
            # ユーザーの入力を履歴に追加
            st.session_state['chat_history'].append(f"あなた: {user_input}")

            # 処理中のグルグル表示 (UX向上)
            with st.spinner("AIが考え中です..."):
                try:
                    # AIに質問を投げる
                    response = model.generate_content(user_input)

                    # AIの返事も履歴に追加
                    st.session_state['chat_history'].append(f"AI: {response.text}")

                    # 結果を表示する
                    st.success("回答が来ました！")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")
        else:
            st.warning("文字を入力してから送信ボタンを押してください。")