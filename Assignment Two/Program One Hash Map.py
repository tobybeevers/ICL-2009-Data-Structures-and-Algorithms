import csv

# Load CSV into a hash map (dictionary)
rainfall_data = {}

with open("wales_rainfall_data.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row["Year"])
        month = row["Month"].lower()
        county = row["County"]
        rainfall = float(row["Rainfall (mm)"])
        
        # Store in hash map with (year, month, county) as the key
        rainfall_data[(year, month, county)] = rainfall

# Example Usage:
print("Rainfall in Cardiff for January 2015:", rainfall_data.get((2015, "january", "Cardiff")))
print("Rainfall in Swansea for February 2016:", rainfall_data.get((2016, "february", "Swansea")))
