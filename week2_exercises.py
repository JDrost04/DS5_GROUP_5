# EXERCISE 1

"""
This script reads a file containing student records, it performs various
calculations and generates a report after some data manipulation.
It shows the average grade and tells you the names of the students 
who scored above a given minimum grade.

This tool only accepts comma separated value files (.csv)
"""

file_path = input("Enter the path to the CSV file: ")        
def read_csv(file_path) -> list:
    """ Reads the CSV file from the given file path and returns a list 
        of student records.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        list: A list of dictionaries where each dictionary represents a 
        student record.
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


def calculate_average(records) -> float:
    """ Calculates the average grade from a list of student records.
    
    Args:
        records (list): A list of dictionaries, each representing a 
        student record.
        
    Returns:
        float: The average grade of all the students.
    """
    
    total = sum(float(record['Grade']) for record in records)
    return total / len(records) if records else 0.0


def filter_records(records, min_grade) -> list:
    """ Filters the student records that have a grade greater than or 
        equal to the specified minimum grade.
       
    Args:
        records (list): A list of dictionaries, each representing 
        a student record.
        min_grade (float): The minimum grade to filter the records.
        
    Returns:
        list: A list of dictionaries representing the filtered 
        student records, only containing the students that have 
        a grade greater than or equal to the specified minimum grade.
    """
    
    return [record for record in records if float(record['Grade']) >= min_grade]


def display_report(average, filtered_records) -> list:
    """ Displays the average grade and a report of students who meet 
        the grade criteria.

    Args:
        average (float): The average grade of all students.
        filtered_records (list): A list of dictionaries representing 
        students who have passed the filter.
    
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
    """ Main function to execute the student grade report generation 
        process. 
        Asks for the file path, reads the student records, calculates 
        the average, filters records, and displays the report.
    
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


# EXERCISE 2

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter) -> int:
    """_summary_

    Args:
        c (_type_): _description_
        max_iter (_type_): _description_

    Returns:
        int: _description_
    """
    a = 0
    for n in range(max_iter):
        if abs(a) > 2:
            return n
        a = a**2 + c
    return max_iter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, max_iter) -> np.ndarray:
    """_summary_

    Args:
        xmin (_type_): _description_
        xmax (_type_): _description_
        ymin (_type_): _description_
        ymax (_type_): _description_
        width (_type_): _description_
        max_iter (_type_): _description_

    Returns:
        np.ndarray: _description_
    """    
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((width, width))
    
    for i in range(width):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)
    
    return mset
   

def draw_mandel(width: int):
    """_summary_

    Args:
        width (int): _description_
    """    
    xmin, xmax, ymin, ymax = -1.5, 0.5, -1, 1
    max_iter = 100

    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, max_iter)

    plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='inferno')
    plt.colorbar()
    plt.title(f'Mandelbrot Visualization (Resolution: {width}x{width})')
    plt.xlabel('Real(c)')
    plt.ylabel('Imaginary(c)')
    plt.show()

draw_mandel(200)


# EXERCISE 3

import week2_exercise3

