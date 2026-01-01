try:
    # エラーが起きそうな処理をここに書く
    a = float(input("割られる数: "))
    b = float(input("割る数: "))
    result = a / b
    print(f"結果: {result}")

except ZeroDivisionError:
    # 0で割ろうとしたときの専用エラー
    print("エラー: 0で割ることはできません！")

except ValueError:
    # 文字列を数値に変換できなかった時のエラー
    print("エラー: 有効な数字を入力してください！")

print("プログラムを終了します。")