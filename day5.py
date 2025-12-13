# 関数の定義（設計図を作る）
def greet(name):
    message = f"こんにちは、{name}さん！"
    return message

# 関数の実行（実際に使う）
result = greet("佐藤") # "佐藤"という材料を渡す
print(result)           # -> "こんにちは、佐藤さん！"