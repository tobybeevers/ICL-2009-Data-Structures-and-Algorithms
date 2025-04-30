"""
Program Four Graph Representation - Adjacency List Implementation for Seasonal Precipitation Data
STEP 1: Import pandas for data manipulation and analysis, numpy for numerical operations, and defaultdict from collections for creating adjacency lists.
"""
import pandas as pd  
from collections import defaultdict  
import numpy as np  

"""
STEP 2: Load the Excel file into a pandas DataFrame. The file "Data 2.xlsx" is located in the "Assignment Two" folder, and the data is read from the sheet named "Sheet1".
"""
data = pd.read_excel(r"Assignment Two/Data 2.xlsx", sheet_name="Sheet1")

"""
STEP 3:
Create an adjacency list to store connections between years based on similarity. The keys will be years, and the values will be lists of tuples (connected year, similarity score).
Then define the months to consider for similarity calculations
"""
monthly_adjacency = defaultdict(list)
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

"""
STEP 4:
Define a function to calculate the Euclidean distance between two rows of monthly rainfall data. Calculate the Euclidean distance between two rows of monthly rainfall data. This function measures the similarity between two years based on their monthly rainfall patterns.
  Parameters:
    - row1: First row of data (Pandas Series)
    - row2: Second row of data (Pandas Series)
    
  Returns:
    - Euclidean distance (float) or infinity if any month's data is missing
"""
def monthly_similarity(row1, row2): 
    distance = 0  # Initialise the distance to zero
    for month in months:
        val1 = row1[month]  # Rainfall value for the current month in row1
        val2 = row2[month]  # Rainfall value for the current month in row2
        # Skip calculation if either value is missing (NaN)
        if pd.isna(val1) or pd.isna(val2):
            return float('inf')  # Return infinity to indicate no similarity
        # Add the squared difference to the distance
        distance += (val1 - val2)**2
    # Return the square root of the total distance (Euclidean distance)
    return np.sqrt(distance)

"""
STEP 5:
Build the adjacency list by comparing each pair of years. The adjacency list will represent the connections between years based on their similarity scores.Define a threshold for similarity, years with a Euclidean distance below this threshold will be considered similar.
"""
SIMILARITY_THRESHOLD = 200  # Adjust this value based on the data's distribution

for i in range(len(data)):
    for j in range(i+1, len(data)):  # Compare each year with all subsequent years
        year1 = data.iloc[i]['year']  # Year of the first row
        year2 = data.iloc[j]['year']  # Year of the second row
        # Calculate the similarity (Euclidean distance) between the two years
        distance = monthly_similarity(data.iloc[i], data.iloc[j])
        
        # If the distance is below the threshold, add the connection to the adjacency list
        if distance <= SIMILARITY_THRESHOLD:
            monthly_adjacency[year1].append((year2, distance))  # Add year2 to year1's connections
            monthly_adjacency[year2].append((year1, distance))  # Add year1 to year2's connections

# Convert the defaultdict to a regular dictionary for cleaner output
monthly_adjacency = dict(monthly_adjacency)

"""
STEP 6:
Display the connections for each year in the adjacency list. The output will show the year and its connections to other years along with the similarity score (distance).
To make changes follow these steps:
  1. Adjust the SIMILARITY_THRESHOLD to control the sensitivity of the connections. A lower value will result in fewer connections, while a higher value will include more years.
  2. Modify the number of connections displayed for each year by changing the slice in the print statement.
  For example, to show the top 3 connections, change [:3] to [:5].
"""
# Example output: Display connections for the first 5 years in the adjacency list
for year in sorted(monthly_adjacency.keys())[:5]:  # Sort years and take the first 5
    # Sort connections by similarity score (distance) and take the top most similar years
    connections = sorted(monthly_adjacency[year], key=lambda x: x[1])
    print(f"{year} -> {connections[:5]}")  # Print the year and its toP connections