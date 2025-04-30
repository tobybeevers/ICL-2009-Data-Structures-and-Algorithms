"""
Program Three Hash Table with Chaining Implementation for Seasonal Precipitation Data
STEP 1: Import pandas for data manipulation and analysis
"""
import pandas as pd

"""
STEP 2: Define a class to represent a hash table with chaining for seasonal precipitation data. The purpose of the SeasonalHashTable Class is to implement a hash table that uses chaining to handle collisions. Each entry in the hash table stores:
    Key-Value Pairs:
        Each entry in the hash table is a list of tuples, where each tuple contains a key (year) and its corresponding value (precipitation data).
    Hash Function:
        The hash function computes the index for a given key (year) by taking the modulus of the key with the size of the hash table.
    Insert Method:
        The insert method adds a new key-value pair to the hash table. If the key already exists, it updates the value.
    Get Method:     
        The get method retrieves the value associated with a given key (year). If the key is not found, it returns None.

"""
class SeasonalHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)] # Create a list of empty lists for chaining
        """
        Initialise the hash table with a specified size.
        Each index in the table is a list to handle collisions using chaining.
        :param size: The size of the hash table (default is 100).
        """       
    def _hash(self, key):
        return key % self.size # Use modulo operation to ensure the index is within table size
        """
        Compute the hash value for a given key.
        :param key: The key to hash (e.g., a year).
        :return: The hash value (index in the table).
        """

    def insert(self, year, data):
        index = self._hash(year) # Compute the hash index
        for i, (k, v) in enumerate(self.table[index]):
            if k == year: # If the key already exists, update the value
                self.table[index][i] = (year, data)
                return
        self.table[index].append((year, data)) # If key doesn't exist, append the new key-value pair
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        :param year: The key (e.g., year).
        :param data: The value (e.g., precipitation data for the year).
        """

    def get(self, year): # Compute the hash index
        index = self._hash(year)
        for k, v in self.table[index]:
            if k == year: # If the key is found, return the value
                return v
        return None # Return None if the key is not found
        """
        Retrieve the value associated with a given key.
        :param year: The key to look up (e.g., year).
        :return: The value (e.g., precipitation data) or None if the key is not found.
        """ 
#########################################

"""
STEP 3: Load the Excel file into a pandas DataFrame. The file "Data 2.xlsx" is located in the "Assignment Two" folder, and the data is read from the sheet named "Sheet1".
"""
df = pd.read_excel(r"Assignment Two/Data 2.xlsx", sheet_name="Sheet1")

"""
STEP 4: Reshape/Clean the DataFrame to extract month, year, and rainfall values. Use a loop to iterate through the columns in pairs (month & year) and create a new DataFrame with the reshaped data.
""" 
hash_table = SeasonalHashTable(size=100) # Create an instance of the hash table with size 100

# Populate the hash table with data from the DataFrame
for _, row in df.iterrows():
    """
    Iterate through each row in the DataFrame.
    Extract the year and precipitation data, and store them in the hash table.
    """

    year = row['year']
    # Extract the year from the current row
    # Create a dictionary to store monthly, seasonal, and annual precipitation data
    data = {
        'monthly': {
            'jan': row['jan'],
            'feb': row['feb'],
            'mar': row['mar'],
            'apr': row['apr'],
            'may': row['may'],
            'jun': row['jun'],
            'jul': row['jul'],
            'aug': row['aug'],
            'sep': row['sep'],
            'oct': row['oct'],
            'nov': row['nov'],
            'dec': row['dec']
        },
        'seasonal': {
            'win': row['win'],
            'spr': row['spr'],
            'sum': row['sum'],
            'aut': row['aut']
        },
        'annual': row['ann']
    }
    hash_table.insert(year, data) # Insert the year and its data into the hash table

"""
STEP 5: Retrieve and display data for a specific year using the hash table.
The lookup_year_data function takes a year as input and retrieves the corresponding data from the hash table. If the year is found, it prints the monthly, seasonal, and annual precipitation data. If not, it indicates that no data was found for that year.
"""

def lookup_year_data(year):
    year_data = hash_table.get(year)
    if year_data is not None:
        print(f"\nData for {year}:")
        print("Monthly Precipitation:")
        for month, value in year_data['monthly'].items():
            print(f"{month}: {value}")
        print("\nSeasonal Totals:")
        for season, value in year_data['seasonal'].items():
            print(f"{season}: {value}")
        print(f"\nAnnual Total: {year_data['annual']}")
    else:
        print(f"No data found for {year}")

# Enter a year to look up (e.g., 2000):
lookup_year_data(1894)

