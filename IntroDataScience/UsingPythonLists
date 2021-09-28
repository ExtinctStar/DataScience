# Program used as the introduction to Data Science with Python
# Takes basic CSV file and outputs basic formatted data
# Author: ExtinctStar

# Allows use of re package to use with Regular Expressions
import re

# Opens the .csv file and automatically closes the file using 'with' statement
# Copies all lines to a List of items in 'content'
with open('Berkeley.csv', mode = 'r', encoding = 'utf-8') as f:
    content = f.readlines()

# Outputs all Raw Data from Data File, skipping the first line
items = []
for i in range(1,len(content)):
    items.append(content[i]) 
print("Raw Data from Data File:\n")
print(items)
print("\n")

# admitted_female_string: string used to search all data for matching line
# Outputs all list elements with matching substring
admitted_female_string = "Admitted,Female"
admitted_female = []
for i in items:
    if admitted_female_string in i:
        admitted_female.append(i.replace("\n", ""))
# admitted_female = [i for i in items if admitted_female_string in i]
print("List of Data Items that include 'Admitted,Female':\n")
print(admitted_female)
print("\n")

# Outputs a 2D List by using the delimiter ',' in re.split
admitted_female_data = []
for i in admitted_female:
    admitted_female_data.append(re.split(",", i))
print("2D List of Usable Admitted Female Data:\n")
print(admitted_female_data)
print("\n")

# Using admitted_female_data, we output all relevant data using the
# index and value of each list element using enumerate()
print("Final Output of Data:\n")
for row_index, row in enumerate(admitted_female_data):
    print("The Number of Admitted Females for Department " + str(admitted_female_data[row_index][2]) + 
          " is " + str(admitted_female_data[row_index][3]))
