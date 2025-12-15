import random

name = input("あなたの名前は？")

# おみくじの中身をリストで作る
fortunes = ["大吉", "中吉", "小吉", "凶", "大凶"]

# リストからランダムに一つ選ぶ
result = random.choice(fortunes)
number = random.randint(1, 100)

# 結果を表示
print(f"{name}さんの運勢は...{result}です！")
print(f"{name}のラッキーナンバーは{number}です")