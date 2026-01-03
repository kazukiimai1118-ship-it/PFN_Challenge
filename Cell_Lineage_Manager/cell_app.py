import streamlit as st
import pandas as pd
from cell_manager import CellManager

# ページ設定 (ブラウザのタブ名などを設定)
st.set_page_config(page_title="Cell Lineage Manager", layout="wide")

# マネージャーの初期化
manager = CellManager()

# タイトル
st.title("Cell Lineage Manager")

# --- サイドバー: 新規細胞登録 ---
st.sidebar.header("新規細胞登録")

with st.sidebar.form("register_form"):
    # 入力項目
    cell_type = st.text_input("細胞種名 (Cell Type)", placeholder="例: HeLa, HEK293T")
    label = st.text_input("ラベル (任意)", placeholder="例: Lot.3, GFP(+)")
    passage = st.number_input("継代数 (Passage)", min_value=0, value=0)
    seeded_count = st.number_input("播種細胞数 (Seeded)", min_value=1000, value=500000, step=10000)

    # 登録ボタン
    submitted = st.form_submit_button("登録する")

    if submitted:
        if cell_type:
            # マネージャーを使って保存
            manager.add_cell(cell_type, label, passage, seeded_count)
            st.sidebar.success(f"{cell_type}を登録しました！")
        else:
            st.sidebar.error("細胞種名は必須です。")

# --- メイン画面: データ一覧表示 ---
st.header("培養中の細胞一覧")

# データを取得
cells = manager.get_all_cells()

if cells:
    # 見やすいようにPandasデータフレームに変換
    df = pd.DataFrame(cells)

    # 表示したい列だけ選んで、列名を日本語にする (オプション)
    display_columns = {
        "id": "ID",
        "cell_type": "細胞種",
        "label": "ラベル",
        "passage": "継代数",
        "seeded_count": "播種数",
        "date": "開始数",
        "status": "状態"
    }

    # データフレームを表示 (use_container_width=Trueで横幅いっぱいに)
    st.dataframe(
        df[display_columns.keys()].rename(columns=display_columns),
        use_container_width=True
    )
else:
    st.info("まだ登録された細胞はありません。サイドバーから登録してください。")

# デバッグ用: JSONの中身をそのまま表示 (開発中のみ便利)
st.write(cells)