import streamlit as st

# タイトルの表示
st.title("PFNへの道: 最初のWebアプリ")

# テキストの表示
st.write("こんにちは！これはPythonだけで作ったWebページです。")
st.write("ここから三か月で、教育エンジニアを目指します！")

# インタラクティブな要素 (チェックボックス)
if st.checkbox("覚悟はできていますか？"):
    st.success("素晴らしい！一緒に頑張りましょう！")