numbers = [110, 2, 3, 12, 80]

while True:
    a=input("数字を入力してください。qを押すと終了")
    if a=="q":
        break
    try:
        a=int(a)
    except ValueError:
        print("数字を入力するか、qを入力してください。")
        continue
    if a in numbers:
        print("正解")
    else:
        print("不正解")
