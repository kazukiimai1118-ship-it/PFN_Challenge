# 設計図 (クラス) を作る
class Dog:
    # 初期化メソッド (コンストラクタ) :インスタンスが生まれた瞬間に呼ばれる
    def __init__(self, name, breed):
        self.name = name    # 自分自身のnameに、渡されたnameを代入
        self.breed = breed  # 自分自身のbreedに、渡されたbreedを代入

    # メソッド (このクラスができる動作)
    def bark(self):
        # self.nameを使うことで、自分自身の名前を呼べる
        print(f"ワン！私は{self.breed}の{self.name}だワン！")

# --- ここからメインの処理 ---       

# インスタンス化 (実態を作る)
my_dog = Dog("ポチ", "柴犬")
friend_dog = Dog("レックス", "シェパード")

# それぞれの動作を呼び出す
my_dog.bark()
friend_dog.bark()