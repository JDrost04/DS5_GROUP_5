#Opdracht 3
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt

N = 400
M = 4
n0 = 5

NW = nx.star_graph(n0)
newnodes = []
for i in range(N-6):
    newnodes.append(i+6)
NW.add_nodes_from(newnodes)
for i in range(1,N):
    if len(list(nx.all_neighbors(NW,i))) <M:
        for j in range((N-1)-i):
            if len(list(nx.all_neighbors(NW,N-(j+1)))) <M:
                NW.add_edge(i,N-(j+1))
            if len(list(nx.all_neighbors(NW,i))) ==M:
                break

for i in range(N):
    print(len(list(nx.all_neighbors(NW,i))))

'''for i in range(n0):
    NW.add_edge(i,i+1)
NW.add_edge(1,n0)
for j in range(int((N/5)-1)):
    list = []
    for i in range(1,6):
        list.append(5+5*j+i)
    NW.add_nodes_from(list)
    for i in range(5):
        NW.add_edge(list[i],list[i-1])
    for i in range(5):
        NW.add_edge(list[i],list[i]-5)'''

nx.draw(NW)
plt.show()