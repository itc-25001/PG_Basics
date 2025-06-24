星座リスト=["","山羊","水瓶","魚","牡羊","牡牛","双子","蟹","獅子","乙女","天秤","蠍","射手"]
month=int(input("月を入力してください"))
day=int(input("日を入力してください"))
星座=星座リスト[month]
if   month == 1  and day >= 20: 星座 =星座リスト [2]
elif month == 2  and day >= 19: 星座 =星座リスト[3] 
elif month == 3  and day >= 21: 星座 =星座リスト[4] 
elif month == 4  and day >= 20: 星座 =星座リスト[5] 
elif month == 5  and day >= 21: 星座 =星座リスト[6] 
elif month == 6  and day >= 22: 星座 =星座リスト[7] 
elif month == 7  and day >= 23: 星座 =星座リスト[8] 
elif month == 8  and day >= 23: 星座 =星座リスト[9] 
elif month == 9  and day >= 23: 星座 =星座リスト[10]
elif month == 10 and day >= 24: 星座 =星座リスト[11]
elif month == 11 and day >= 23: 星座 =星座リスト[12]
elif month == 12 and day >= 22: 星座 =星座リスト[1] 

print(f"あなたの星座は{星座}です。")


