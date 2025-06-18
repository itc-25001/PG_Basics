import csv

movies=[
	["Top Gun","Risky Business","Minority Report"],
	["Titanic","The Revenant","Inception"],
    ["Training Day","Man on Fire","Flight"]
        ]
with open("c3.csv","w",newline='') as a:
    w=csv.writer(a,delimiter=",")
    for b in movies:
        w.writerow(b)

