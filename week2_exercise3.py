#Opdracht 3
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt

N = 400
M = 4
n0 = 5

def graph_generator(N,M,n0):
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
    return NW

nx.draw(graph_generator(N,M,n0))
plt.show()