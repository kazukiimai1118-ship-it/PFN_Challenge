import streamlit as st

st.title("Day 16: ユーザー入力の基本")

# 1. テキスト入力フォーム (Text Input)
# 変数 = st.text_input("ラベル")の形で使います
name = st.text_input("あなたのお名前を教えてください")
hobby = st.text_input("今、夢中になっていることは？")
age = st.number_input("あなたのご年齢を教えてください", value=20, step=1)

# 2. ボタン (Button)
# ボタンが押された瞬間だけ True になる
if st.button("送信する"):
    # 3. 条件分岐と表示
    # 名前と趣味が両方入力されているかチェック
    if name and hobby and age:
        st.success(f"こんにちは、{name}さん！あなたは{age}歳なんですね！")
        st.write(f"{hobby}、いいですね！PFNのエンジニアも{hobby}が好きかもしれませんよ。")
        # 派手な演出 (風船が飛びます)
        st.balloons()
    else:
        st.error("お名前と趣味と年齢のすべてを入力してください！")