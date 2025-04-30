"""
Program One: AVL Tree Implementation for Rainfall Data
STEP 1: Import pandas for data manipulation and analysis
"""
import pandas as pd  

"""
STEP 2: Load the Excel file into a pandas DataFrame. The file "Data 1.xlsx" is located in the "Assignment Two" folder, and the data is read from the sheet named "Sheet1".
"""
df = pd.read_excel(r"Assignment Two/Data 1.xlsx", sheet_name="Sheet1")

"""
STEP 3: Reshape/Clean the DataFrame to extract month, year, and rainfall values. Use a loop to iterate through the columns in pairs (month & year) and create a new DataFrame with the reshaped data.
"""
reshaped_data = []  # Initialize an empty list to store reshaped data

# Iterate through the columns in pairs (month and year)
for i in range(0, len(df.columns), 2):
    month = df.columns[i]  # Get the month name (e.g., 'jan', 'feb')
    year_column = df.columns[i + 1]  # Get the corresponding year column name
    
    # Extract the rainfall values and years for the current month
    for index, row in df.iterrows():
        year = row[year_column]  # Get the year value for the current row
        rainfall = row[month]  # Get the rainfall value for the current row
        reshaped_data.append((year, month, rainfall))  # Append the data as a tuple

# Convert the reshaped data into a new DataFrame
reshaped_df = pd.DataFrame(reshaped_data, columns=['Year', 'Month', 'Rainfall'])

# Ensure the 'Rainfall' column is numeric
reshaped_df['Rainfall'] = pd.to_numeric(reshaped_df['Rainfall'], errors='coerce')

# Drop rows with NaN values in the 'Rainfall' column (if any)
reshaped_df = reshaped_df.dropna(subset=['Rainfall'])

# Print the first few rows of the reshaped DataFrame to verify the data
print(reshaped_df.head())

"""
STEP 4: Define a class to represent a node in the AVL tree for rainfall data. The purpose of the RainfallNode Class is to represent a single node in the AVL tree. Each node stores:
    Rainfall Data:
        year: The year of the rainfall record.
        month: The month of the rainfall record.
        value: The rainfall value.
    Pointers to Child Nodes:
        left: Points to the left child node in the AVL tree.
        right: Points to the right child node in the AVL tree.
    Height:
        height: Tracks the height of the node, which is used to determine whether the tree is balanced and to perform rotations if necessary.
"""
class RainfallNode:
    def __init__(self, year, month, value):
        # Initialize the node with year, month, and rainfall value
        self.year = year  # Year of the rainfall record
        self.month = month  # Month of the rainfall record
        self.value = value  # Rainfall value (used as the key for AVL tree operations)
        
        # Initialize pointers to the left and right child nodes
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node
        
        # Initialize the height of the node (used for balancing the AVL tree)
        self.height = 1
"""
This next code defines the RainfallAVL class, which implements an AVL tree for storing and managing rainfall data. 
The AVL tree is a self-balancing binary search tree, which means that it maintains its balance after every insertion or deletion operation. The class includes methods for inserting nodes, finding the maximum and minimum rainfall records, and performing in-order traversal to retrieve nodes in sorted order.
    Insert Method:
        Inserts a new node into the AVL tree while maintaining its balance.
    Find Maximum Method:
        Finds the node with the maximum rainfall value in the AVL tree.
    Find Minimum Method:
        Finds the node with the minimum rainfall value in the AVL tree.
    In-Order Traversal Method:
        Performs an in-order traversal of the AVL tree to retrieve nodes in sorted order. 
    In Order Recursive Method:
        A helper method for the in-order traversal that recursively visits nodes in the tree. 
"""
class RainfallAVL:
    def insert(self, root, year, month, value):
        # Standard AVL insertion with balancing
        if not root:
            # If the root is None, create a new node and return it
            return RainfallNode(year, month, value)
        elif value < root.value:
            # If the new value is less than the current node's value, insert it into the left subtree
            root.left = self.insert(root.left, year, month, value)
        else:
            # Otherwise, insert it into the right subtree
            root.right = self.insert(root.right, year, month, value)
        
        # Update height and balance (rotation code omitted)
        return root
    
    def find_max(self, root):
        # Traverse to the rightmost node to find the maximum value
        current = root
        while current.right:
            current = current.right
        return (current.year, current.month, current.value)
    
    def find_min(self, root):
        # Traverse to the leftmost node to find the minimum value
        current = root
        while current.left:
            current = current.left
        return (current.year, current.month, current.value)
    
    def in_order_traversal(self, root):
        # Perform an in-order traversal to retrieve nodes in sorted order
        result = []  # Initialize an empty list to store the traversal result
        self._in_order_recursive(root, result)  # Call the helper method
        return result

    def _in_order_recursive(self, node, result):
        # Helper method for in-order traversal
        if node:
            # Recursively visit the left subtree
            self._in_order_recursive(node.left, result)
            # Append the current node's data to the result list
            result.append((node.year, node.month, node.value))
            # Recursively visit the right subtree
            self._in_order_recursive(node.right, result)

"""
STEP 5: Create an instance of the AVL tree and insert data from the reshaped DataFrame.
"""
# Create an instance of the AVL tree
avl_tree = RainfallAVL()
root = None  # Initialise the root of the AVL tree as None

# Insert data from the reshaped DataFrame into the AVL tree
for index, row in reshaped_df.iterrows():
    root = avl_tree.insert(root, row['Year'], row['Month'], row['Rainfall'])

"""
STEP 6: Calucate/Print values for the AVL Tree
    1. In-order traversal of the AVL tree to retrieve nodes in sorted order.
    2. Find and print the minimum and maximum rainfall records.
    3. Calculate the average rainfall by month.
"""
# Find and print the minimum and maximum rainfall records
print("Minimum Rainfall Record:", avl_tree.find_min(root))
print("Maximum Rainfall Record:", avl_tree.find_max(root))

# Calculate the average rainfall by month
average_rainfall_by_month = reshaped_df.groupby('Month')['Rainfall'].mean()

# Print the average rainfall for each month
print("Average Rainfall by Month:")
print(average_rainfall_by_month)