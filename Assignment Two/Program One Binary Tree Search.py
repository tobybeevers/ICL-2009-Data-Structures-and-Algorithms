class BSTNode:
    def __init__(self, year, month, county, rainfall):
        self.year = year
        self.month = month
        self.county = county
        self.rainfall = rainfall
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, year, month, county, rainfall):
        """Insert a new (year, month, county) node in the BST."""
        if not self.root:
            self.root = BSTNode(year, month, county, rainfall)
        else:
            self._insert(self.root, year, month, county, rainfall)

    def _insert(self, node, year, month, county, rainfall):
        """Recursive helper function for inserting into BST."""
        if (year, month, county) < (node.year, node.month, node.county):
            if node.left is None:
                node.left = BSTNode(year, month, county, rainfall)
            else:
                self._insert(node.left, year, month, county, rainfall)
        else:
            if node.right is None:
                node.right = BSTNode(year, month, county, rainfall)
            else:
                self._insert(node.right, year, month, county, rainfall)

    def search(self, year, month, county):
        """Search for a (year, month, county) node."""
        return self._search(self.root, year, month, county)

    def _search(self, node, year, month, county):
        """Recursive helper function for searching in BST."""
        if not node:
            return None
        if (year, month, county) == (node.year, node.month, node.county):
            return node.rainfall
        elif (year, month, county) < (node.year, node.month, node.county):
            return self._search(node.left, year, month, county)
        else:
            return self._search(node.right, year, month, county)

# Load CSV into BST
import csv

bst = BST()

with open("wales_rainfall_data.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row["Year"])
        month = row["Month"].lower()
        county = row["County"]
        rainfall = float(row["Rainfall (mm)"])
        bst.insert(year, month, county, rainfall)

# Example Usage
print("Rainfall in Cardiff for January 2015:", bst.search(2015, "january", "Cardiff"))
print("Rainfall in Swansea for February 2016:", bst.search(2016, "february", "Swansea"))
