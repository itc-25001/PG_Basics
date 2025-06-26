import random

def hangman():
    words = ["apple", "banana", "cherry", "grape", "orange"]  # 単語リスト
    word = random.choice(words)  # ランダムに1単語選ぶ
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\\     ",
              "|       / \\     ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            idx = rletters.index(char)
            board[idx] = char
            rletters[idx] = '$'  # 一度使った文字の処理
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0: wrong + 1]))

        if "_" not in board:
            print("あなたの勝ち！正解は「{}」でした。".format(word))
            win = True
            break

    if not win:
        print("\nあなたの負け！正解は「{}」でした。".format(word))

hangman()





