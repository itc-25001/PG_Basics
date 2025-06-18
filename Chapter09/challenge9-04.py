import csv

movies=[
    ["トップガン","リスキービジネス","マイノリティーレポート"],
    ["タイタニック","ザレベナント","インセプション"],
    ["トレーニング・デイ","マンオンファイア","飛行"]
        ]
with open("c4.csv","w",newline='') as a:
    w=csv.writer(a,delimiter=",")
    for b in movies:
        w.writerow(b)

