def calculate_area(width, height):
    area = width * height
    return area

# 関数の外で呼び出す
area = calculate_area(10, 5)
print(f"面積は{area}です")