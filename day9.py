# ファイルへの書き込み ('w'は上書きモード, 'a'は追記モード)
#　encounting='utf-8' は日本語を扱う場合に必須です。
diary_content = input("今日の日記を書いてください: ")

with open('diary.txt', 'a', encoding='utf-8') as f:
    f.write(diary_content + "\n") # 改行コード \n を追加

print("保存しました。")

# ファイルの読み込み ('r' モード)
print("--- 過去の日記 ---")
with open('diary.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)