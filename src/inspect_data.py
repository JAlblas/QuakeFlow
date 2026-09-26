import csv

DATA_PATH = "data/raw/all_month.csv"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Columns:", header)
    print()

    for i, row in enumerate(reader):
        print(row)
        print()
        if i >= 4:
            break