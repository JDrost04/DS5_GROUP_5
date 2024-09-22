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
    """Generates the Mandelbrot set value for a given complex number c.
    
    Args:
        c (complex): A complex number representing a point in the complex plane.
        max_iter (int): The maximum number of iterations to check if the point escapes.

    Returns:
        int: The number of iterations before the point escapes, or max_iter if it doesn't escape.
    """
    a = 0
    for n in range(max_iter):
        if abs(a) > 2:
            return n
        a = a**2 + c
    return max_iter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, max_iter) -> np.ndarray:
     """Generates the Mandelbrot set for a given range of the complex plane.
    
    Args:
        xmin (float): Minimum real part of the complex plane.
        xmax (float): Maximum real part of the complex plane.
        ymin (float): Minimum imaginary part of the complex plane.
        ymax (float): Maximum imaginary part of the complex plane.
        width (int): Resolution of the grid (both in real and imaginary axes).
        max_iter (int): Maximum iterations for Mandelbrot set generation.

    Returns:
        np.ndarray: A 2D array representing the Mandelbrot set, where each element
                    represents the number of iterations for each complex point.
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
    """Draws and visualizes the Mandelbrot set with a specified resolution.

    Args:
        width (int): The resolution of the generated Mandelbrot set image.
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
# 3.1
import pandas as pd
import math as m
import networkx as nx
import scipy.stats as sp


N = 400
M = 4
n0 = 5

def create_random_graph(N: int,M: int,n0: int):
    ''' This function creates a graph of connections between points dependent on how many connections a point already has. (the pagerank of each point).
    
    Args:
        N (Type = int): Amount of total points created in the graph.
        M (Type = int): Amount of connections a point starts with. (For example M=4 will create a point with 4 connections to earlier points)
        n0 (Type = int): Amount of points the graph starts with. (For example n0=5 will start the graph with a center point connected to 5 other points)

    Returns:
        NW: The graph with connections based on the pagerank of each point.   
    
    
    
    '''
    NW = nx.star_graph(n0)
    node_amount = n0+1
    #print('yep de werkt nog')
    for i in range(n0+1,N):
        pagerank_chances = nx.pagerank(NW)
        NW.add_node(i)
        link_points = np.random.choice(node_amount,M,replace=False,p=list(pagerank_chances.values()))
        for j in range(M):
            NW.add_edge(i,link_points[j])
        node_amount += 1
        #print(f'je bent nu bij node {node_amount}')
    return NW

NW = create_random_graph(N,M,n0)

nx.draw(NW)
plt.show()

para = nx.pagerank(NW)
df3 = pd.DataFrame.from_dict(para, orient='index', columns=['Pagerank'])
print(df3)


#opdracht 3.2
file_path = input("Please enter the file path to the .csv file:")
def read_and_graph(filepath):
    ''' This function reads a csv file containing unidirectional edges. It returns a networkx DiGraph
    with these edges.
    
    Args:
        filepath (str): The path to the csv file.
    
    Returns:
        G: A graph with the edges from the csv file.
    '''
    df = pd.read_csv(filepath)
    df.columns = ['from', 'to']
    G = nx.DiGraph()
    G.add_nodes_from(df.loc[:,'from'])
    for i in range(len(df)):
       G.add_edge(df.loc[i,'from'],df.loc[i,'to'])
    return G

def pagerank_from_csv(filepath):
    ''' This function reads a csv file containing unidirectional edges and pageranks the nodes.
    
    Args:
        filepath (str): The path to the csv file.
        
    Returns:
        df2: Pandas DataFrame containing nodes and their respective pageranks.
    '''
    pagran = nx.pagerank(read_and_graph(filepath))
    df2 = pd.DataFrame.from_dict(pagran, orient='index', columns=['Pagerank'])
    return df2

print(pagerank_from_csv(file_path))