import csv
import random, datetime

skor = [
    random.choice(["Ali", "Veli", "Ayşe"]),
    datetime.datetime.now().strftime("%H:%M:%S"),
    random.randint(0, 100)
]

print(skor)

with open("skor.csv", "a", encoding="UTF-8") as fw:
    csv.writer(fw, delimiter=";").writerow(skor)

