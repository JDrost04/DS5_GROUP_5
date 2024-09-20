#Opdracht 3.1
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np

N = 400
M = 4
n0 = 5

def create_random_graph(N,M,n0):
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