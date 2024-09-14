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
    
def read_csv(file_path):
    """
    Reads the CSV file from the given file path and returns a list of student records.
    
    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries where each dictionary represents a student record.
    """
    records = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            record = dict(zip(headers, values))
            records.append(record)
    return records

def calculate_average(records):
    """
    Calculates the average grade from a list of student records.
    
    Args:
        records (list): A list of dictionaries, each representing a student record.

    Returns:
        float: The average grade of all the students.
    """
    total = sum(float(record['Grade']) for record in records)
    return total / len(records) if records else 0.0

def filter_records(records, min_grade):
    """
    Filters the student records that have a grade greater than or equal to the specified minimum grade.
    
    Args:
        records (list): A list of dictionaries, each representing a student record.
        min_grade (float): The minimum grade to filter the records.

    Returns:
        list: A list of dictionaries representing the filtered student records.
    """
    return [record for record in records if float(record['Grade']) >= min_grade]

def display_report(average, filtered_records):
    """
    Displays the average grade and a report of students who meet the grade criteria.
    
    Args:
        average (float): The average grade of all students.
        filtered_records (list): A list of dictionaries representing students who have passed the filter.
    
    Returns:
        None
    """
    print(f"Average Grade: {average}")
    print("--------------------")
    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")

def main():
    """
    Main function to execute the student grade report generation process.
    Asks for the file path, reads the student records, calculates the average, filters records,
    and displays the report.
    
    Args:
        None
    
    Returns:
        None
    """
    file_path = input("Enter the path to the CSV file: ")
    records = read_csv(file_path)
    average = calculate_average(records)
    filtered_records = filter_records(records, min_grade=80.0)
    display_report(average, filtered_records)

if __name__ == "__main__":
    main()


# Exercise 2: Mandelbrot visualisation



# EXERCISE 3: Google PageRank algorithm and the worldwide web
#3.1




#3.2




