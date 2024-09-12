# Exercise 1

"""
Exercise 1: Structuring a given code
You have been given a code (see below) that reads a CSV file containing student records,
performs various calculations and generates a report after some data manipulation.
However, the code is complex, difficult to understand and missing documentation.
For this exercise, perform the following tasks:
1. Work in Github from the start
2. Break down the code into smaller functions
3. Add descriptive docstrings to each function and type hints for your functions
Note, even though you do not have the student records available, you should be able to
break a working code up and add descriptive docstrings.
Code:
"""

file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)
        
total = sum(float(record['Grade']) for record in records)
average = total / len(records)
print(f"Average Grade: {average}")
print("--------------------")
filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
print("Student Report")
print("--------------")
for record in filtered_records:
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")
    
    

# Exercise 2: Mandelbrot visualisation



# EXERCISE 3: Google PageRank algorithm and the worldwide web
#3.1




#3.2




