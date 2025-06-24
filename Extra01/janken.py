#最初にrandomモジュールを呼び出す(乱数のため)
import random
hands=["👊","✌","🖐"]
#input文で人間側のじゃんけんの手を入力させ、変数にいれる
a=int(input("じゃんけんの番号を入力してください。(0/1/2)"))
print("0:グー、1:チョキ、2:パー")
#乱数でコンピューター側のじゃんけんの手を決め、変数にいれる
computer=random.randint(0,2)
#勝敗判定
print(f"あなたの手:{hands[a]}")
print(f"コンピューターの手:{hands[computer]}")
#👊
if a==0:
    if computer==0:
        print("あいこ")
    elif computer==1:
        print("勝ち")
    else:
        print("負け")
#✌
if a==1:
    if computer==0:
        print("負け")
    elif computer==1:
        print("あいこ")
    else:
        print("勝ち")
#🖐
if a==2:
    if computer==0:
        print("勝ち")
    elif computer==1:
        print("負け")
    else:
        print("あいこ")

