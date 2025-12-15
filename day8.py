import random # randomモジュールを読み込む

# おみくじの中身をリストで作る
fortunes = ["大吉", "中吉", "小吉", "凶", "大凶"]

# リストからランダムに一つ選ぶ
result = random.choice(fortunes)

# 結果を表示
print(f"今日の運勢は...{result}です！")