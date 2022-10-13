import csv

with open("skor.csv", "r", encoding="UTF-8") as fr:
    for satir in csv.reader(fr, delimiter=";"):
        if satir:
            print(f"{satir[0]:.1s}** --> {satir[2]}")

