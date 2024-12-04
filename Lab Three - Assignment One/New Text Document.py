
## Import the matplotlib library and venn digram function
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Create a List with the CSV data, this is a two dimensiotional array
# Data preparation: Each person is categorised by their responses to 
# "Safe for Vaccine", "Faith in Vac-Jab1", "Faith in Vac-Jab2"

data = [
    (1, 'Yes', 'Yes', 'Yes'),
    (2, 'Yes', 'Yes', 'No'),
    (3, 'Yes', 'No', 'Yes'),
    (4, 'No', 'Yes', 'No'),
    (5, 'No', 'No', 'Yes'),
    (6, 'No', 'Yes', 'Yes'),
    (7, 'Yes', 'No', 'No'),
    (8, 'No', 'No', 'No'),
    (9, 'No', 'No', 'Yes'),
    (10, 'No', 'Yes', 'Yes'),
    (11, 'Yes', 'No', 'No'),
    (12, 'No', 'No', 'No'),
    (13, 'Yes', 'Yes', 'Yes'),
    (14, 'Yes', 'Yes', 'No'),
    (15, 'Yes', 'Yes', 'Yes'),
    (16, 'Yes', 'Yes', 'No'),
    (17, 'Yes', 'Yes', 'Yes'),
    (18, 'Yes', 'Yes', 'No'),
    (19, 'Yes', 'No', 'Yes'),
    (20, 'No', 'Yes', 'No'),
    (21, 'No', 'No', 'Yes'),
    (22, 'No', 'Yes', 'Yes'),
    (23, 'Yes', 'No', 'No'),
    (24, 'No', 'No', 'No'),
    (25, 'No', 'Yes', 'No'),
    (26, 'No', 'No', 'Yes'),
    (27, 'No', 'Yes', 'Yes'),
    (28, 'Yes', 'No', 'No'),
    (29, 'No', 'No', 'No'),
    (30, 'No', 'No', 'Yes'),
    (31, 'No', 'Yes', 'Yes'),
    (32, 'Yes', 'No', 'No'),
    (33, 'No', 'No', 'Yes'),
    (34, 'No', 'Yes', 'Yes'),
    (35, 'Yes', 'No', 'No'),
    (36, 'No', 'No', 'No'),
    (37, 'No', 'Yes', 'No'),
    (38, 'No', 'No', 'Yes'),
    (39, 'No', 'Yes', 'Yes'),
    (40, 'Yes', 'No', 'No'),
    (41, 'No', 'No', 'No'),
    (42, 'No', 'No', 'Yes'),
    (43, 'No', 'Yes', 'Yes'),
    (44, 'No', 'No', 'Yes'),
    (45, 'Yes', 'No', 'No'),
    (46, 'No', 'No', 'No'),
    (47, 'No', 'No', 'Yes'),
    (48, 'No', 'Yes', 'Yes'),
    (49, 'Yes', 'No', 'No'),
    (50, 'Yes', 'Yes', 'Yes'),
]

# Create a variable with 0,1 and 2 to hold the values for Yes statements
A = 0  # Safe for Vaccine ('Yes')
B = 1  # Faith in Vac-Jab1 ('Yes')
C = 2  # Faith in Vac-Jab2 ('Yes')

# Initialise a dictionary to track the counts of different intersections
intersections = {
    '100': 0,  # Only A (Safe for Vaccine)
    '010': 0,  # Only B (Faith in Vac-Jab1)
    '001': 0,  # Only C (Faith in Vac-Jab2)
    '110': 0,  # A ∩ B
    '101': 0,  # A ∩ C
    '011': 0,  # B ∩ C
    '111': 0,  # A ∩ B ∩ C
    '000': 0,  # None
}

# Categorising the data based on the three attributes
for person in data:
    safe, jab1, jab2 = person[1], person[2], person[3]
    # Create a binary tuple to represent the three categories
    key = f"{'1' if safe == 'Yes' else '0'}{'1' if jab1 == 'Yes' else '0'}{'1' if jab2 == 'Yes' else '0'}"
    intersections[key] += 1

# Create the Venn diagram using the intersection data
venn = venn3(subsets=(
    intersections['100'],  # Only Safe for Vaccine
    intersections['010'],  # Only Faith in Vac-Jab1
    intersections['110'],  # Safe for Vaccine ∩ Faith in Vac-Jab1
    intersections['001'],  # Only Faith in Vac-Jab2
    intersections['101'],  # Safe for Vaccine ∩ Faith in Vac-Jab2
    intersections['011'],  # Faith in Vac-Jab1 ∩ Faith in Vac-Jab2
    intersections['111'],  # Safe for Vaccine ∩ Faith in Vac-Jab1 ∩ Faith in Vac-Jab2
), set_labels=('Safe for Vaccine', 'Faith in Vac-Jab1', 'Faith in Vac-Jab2'))

# Display the Venn diagram
plt.title("Venn Diagram of Vaccine Attributes")
plt.show()
