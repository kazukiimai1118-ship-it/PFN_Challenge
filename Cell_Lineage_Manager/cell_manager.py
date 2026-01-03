import json
import os
import uuid # 重複しないIDを作るためのライブラリ
from datetime import datetime

# データを保存するファイル名
DATA_FILE = "cells.json"

class CellManager:
    def __init__(self):
        """
        クラスの初期化メソッド
        アプリ起動時に自動的にデータを読み込みます
        """
        self.cells = [] # 全細胞データを格納するリスト
        self.load_data()

    def add_cell(self, cell_type, label, passage, seeded_count, parent_id=None):
        """
        新しい細胞を登録するメソッド
        """
        # ユニークなIDを生成 (例: "c001..."のような文字列)
        new_id = str(uuid.uuid4())[:8]

        # 今日の日付
        today = datetime.now().strftime("%Y-%m-%d")

        # 辞書データを作成 (Day 22の設計に基づく)
        new_cell = {
            "cell_type": cell_type,
            "id": new_id,
            "parent_id": parent_id,
            "label": label,
            "date": today,
            "passage": int(passage),
            "seeded_count": int(seeded_count),
            "harvested_count": None,    # まだ回収していない
            "pdl": 0.0,
            "doubling_time": None,
            "status": "active"
        }

        self.cells.append(new_cell)
        self.save_data()                # 追加したらすぐに保存
        print(f"✅ 細胞を追加しました: {cell_type} (ID: {new_id})")
        return new_cell
    
    def get_all_cells(self):
        """
        全データを返す
        """
        return self.cells
    
    def save_data(self):
        """
        現在のself.cellsの内容をJSONファイルに保存する
        """
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.cells, f, indent=4, ensure_ascii=False)
            # print("データ保存完了") # デバッグ用
        except Exception as e:
            print(f"✖ 保存エラー: {e}")
    
    def load_data(self):
        """
        JSONファイルがあれば読み込んでself.cellにセットする
        """
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.cells = json.load(f)
                print(f"{len(self.cells)}件のデータを読み込みました。")
            except Exception as e:
                print(f"✖ 読み込みエラー: {e}")
                self.cells = []
        else:
            print("🆕 新規データファイルを作成します。")
            self.cells = []

# --- 動作確認用 ---
if __name__ == "__main__":
    manager = CellManager()

    #テスト: 細胞２つを追加してみる
    manager.add_cell("HeLa", "Control", 5, 500000)
    manager.add_cell("iPS-201B7", "Lot.A", 10, 10000)

    # 現在のリストを表示
    print("\n--- 現在の細胞リスト ---")
    for cell in manager.get_all_cells():
        print(cell) 