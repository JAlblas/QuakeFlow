import csv

DATA_PATH = "data/raw/all_month.csv"

valid_rows = 0
skipped_rows = 0

with open(DATA_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            magnitude = float(row["mag"])
            valid_rows += 1
        except ValueError:
            skipped_rows += 1
            continue

print(f"Valid rows: {valid_rows}")
print(f"Skipped rows: {skipped_rows}")