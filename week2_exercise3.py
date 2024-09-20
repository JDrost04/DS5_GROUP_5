#Opdracht 3
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt
import scipy.stats as sp

N = 400
M = 4
n0 = 5

#Opdracht 3.1 random versie
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
'''
N = 20
M = 4
n0 = 5
'''

def create_random_graph(N,M,n0):
    NW = nx.star_graph(n0)
    node_amount = n0+1
    print('yep de werkt nog')
    for i in range(n0+1,N):
        pagerank_chances = nx.pagerank(NW)
        NW.add_node(i)
        link_points = np.random.choice(node_amount,M,replace=False,p=list(pagerank_chances.values()))
        for j in range(M):
            NW.add_edge(i,link_points[j])
        node_amount += 1
        print(f'je bent nu bij node {node_amount}')
    return NW




NW = create_random_graph(N,M,n0)

nx.draw(NW)
plt.show()

para = nx.pagerank(NW)
df3 = pd.DataFrame.from_dict(para, orient='index', columns=['Pagerank'])
print(df3)




#opdracht 3.2
df = pd.read_csv('ds5_assignment_group5/squirrel_edges.csv')
df.columns = ['from', 'to']
G = nx.DiGraph()
G.add_nodes_from(df.loc[:,'from'])
for i in range(len(df)):
    G.add_edge(df.loc[i,'from'],df.loc[i,'to'])

pagran = nx.pagerank(G)
df2 = pd.DataFrame.from_dict(pagran, orient='index', columns=['Pagerank'])
print(df2)
