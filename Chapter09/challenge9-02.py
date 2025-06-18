a=input("あなたの好きな食べ物は？")

with open("food.txt","w") as b:
    b.write(a)
