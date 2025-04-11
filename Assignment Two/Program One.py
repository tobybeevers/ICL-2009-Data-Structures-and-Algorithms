import csv

# Load CSV into a nested dictionary structure
rainfall_data = {}

with open("wales_rainfall_data.csv", mode="r") as file:
    reader = csv.DictReader(file)  # Reads the CSV with column names
    for row in reader:
        year = int(row["Year"])  # Convert year to integer
        month = row["Month"].lower()  # Convert month to lowercase for consistency
        county = row["County"]
        rainfall = float(row["Rainfall (mm)"])  # Convert rainfall to float

        # Initialize the year in the dictionary if it doesn't exist
        if year not in rainfall_data:
            rainfall_data[year] = {}

        # Initialize the month in the year's dictionary if it doesn't exist
        if month not in rainfall_data[year]:
            rainfall_data[year][month] = {}

        # Store the rainfall data for the county
        rainfall_data[year][month][county] = rainfall

# Example Usage:
print("Rainfall in Cardiff for January 2015:", rainfall_data.get(2015, {}).get("january", {}).get("Cardiff"))
print("Rainfall in Swansea for February 2016:", rainfall_data.get(2016, {}).get("february", {}).get("Swansea"))