# ToDo List
# 1. add tasks
# 2. display tasks
# 3. over
# select:

# タスクを保存するリスト（最初は空っぽ）
tasks = []

while True:
    # 1. display menu
    print("\n=== ToDo List ===")
    print("1. タスクを追加")
    print("2. タスクを表示")
    print("3. 終了")

    # 2. ユーザーの入力を受け取る
    choice = input("選択してください: ")

    # 3. 入力によって処理を分岐させる
    if choice == "1":
        # ここでタスク名を入力させ、リストに追加（append）する
        task = input("新しいタスクを入力してください：")
        tasks.append(task)
        
    elif choice == "2":
        # ここでリストの中身をループ表示する
        # ヒント：enumerateを使うと番号も出せる
        # for i, task in enumerate(tasks): ...
        for i, task in enumerate(tasks):
            # print(f"\n{enumerate(i)}. {i}")
            print(f"{i + 1}. {task}")    

    elif choice == "3":
        print("アプリを終了します。")
        break # ループを強制終了する魔法の言葉

    else:
        print("無効な入力です。もう一度入力してください。")