"""
Program Two: Three-Dimensional Array Implementation for Rainfall Data
STEP 1: Import pandas for data manipulation and analysis, and Numpy for numerical operations
"""
import pandas as pd
import numpy as np

"""
STEP 2: Load the Excel file into a pandas DataFrame. The file "Data 1.xlsx" is located in the "Assignment Two" folder, and the data is read from the sheet named "Sheet1".
"""
df = pd.read_excel(r"Assignment Two/Data 1.xlsx", sheet_name="Sheet1")

"""
STEP 3: Reshape/Clean the DataFrame to extract month, year, and rainfall values. Use a loop to iterate through the columns and create a new DataFrame with the reshaped data.
"""
reshaped_data = []  # Initialise an empty list to store reshaped data

# Iterate through the columns in pairs (month & year)
for i in range(0, len(df.columns), 2):
    month = df.columns[i]  # Get the month name (e.g., 'jan', 'feb')
    year_column = df.columns[i + 1]  # Get the corresponding year column name
    
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        year = row[year_column]  # Extract the year value for the current row
        rainfall = row[month]  # Extract the rainfall value for the current row
        reshaped_data.append((year, month, rainfall))  # Append the data as a tuple (Year, Month, Rainfall)

# Convert the reshaped data into a new DataFrame
reshaped_df = pd.DataFrame(reshaped_data, columns=['Year', 'Month', 'Rainfall'])

# Ensure the 'Rainfall' column is numeric
reshaped_df['Rainfall'] = pd.to_numeric(reshaped_df['Rainfall'], errors='coerce')  # Convert non-numeric values to NaN
reshaped_df = reshaped_df.dropna(subset=['Rainfall'])  # Drop rows with NaN values in the 'Rainfall' column

# Get unique years and months from the reshaped DataFrame
years = reshaped_df['Year'].unique()  # Extract unique years
months = reshaped_df['Month'].unique()  # Extract unique months

"""
STEP 4: Define a 3D array to store rainfall data. The dimensions of the array are based on the number of unique years and months. The array is initialised with NaN values to indicate any missing data.
An index is added to the Year and Month arrays to make it easier to access the data.
"""
# Create a 3D array with dimensions (Years x Months x 1) and initialise with NaN
rainfall_3d_array = np.full((len(years), len(months), 1), np.nan)

# Create mappings from years and months to their respective indices
year_to_index = {year: i for i, year in enumerate(years)}  # Map each year to an index
month_to_index = {month: i for i, month in enumerate(months)}  # Map each month to an index

"""
STEP 5: Populate the array with data using a for loop.
"""
# Iterates through the reshaped DataFrame and populate the 3D array
for _, row in reshaped_df.iterrows():
    year_idx = year_to_index[row['Year']]  # Get the index for the year
    month_idx = month_to_index[row['Month']]  # Get the index for the month
    rainfall_3d_array[year_idx, month_idx, 0] = row['Rainfall']  # Assign the rainfall value to the 3D array

# Print the 3D array to verify its structure and contents
print("3D Rainfall Array:")
print(rainfall_3d_array)

"""
STEP 6: Example usage of the 3D array to access rainfall data for a specific year and month. This example demonstrates how to access the rainfall data for January 1948.
"""
# Example: Access rainfall for a specific year and month
example_year = 1948  # Specify the year
example_month = 'jan'  # Specify the month

# Get the indices for the specified year and month
year_idx = year_to_index[example_year]
month_idx = month_to_index[example_month]

# Access and print the rainfall value for the specified year and month
print(f"Rainfall for {example_month} {example_year}: {rainfall_3d_array[year_idx, month_idx, 0]}")