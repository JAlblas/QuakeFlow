import csv

DATA_PATH = "data/raw/all_month.csv"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader):
        print(row["time"], row["place"], row["mag"])
        print()
        if i >= 4:
            break