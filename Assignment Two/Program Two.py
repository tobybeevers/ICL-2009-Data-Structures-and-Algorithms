

rainfall_list = []

with open("Rainfall.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row["Year"])
        monthly_values = [float(row[month]) for month in row if month != "Year"]
        rainfall_list.append((year, monthly_values))

