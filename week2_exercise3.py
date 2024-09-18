#Opdracht 3
import pandas as pd
import math as m
import networkx as nx
import matplotlib.pyplot as plt

NW = nx.star_graph(5)
nx.draw(NW, with_labels=True)
plt.show()