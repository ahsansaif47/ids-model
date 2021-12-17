import networkx as nx
import pandas as pd
import os
from Mat_Package import Grapher
import numpy as np

bG = nx.read_gpickle("./Graph DS/Graph.gpickle")

CSV_Folder = r"./Test Invoices Folder/CSVs/"
csvs = os.listdir(CSV_Folder)
print(CSV_Folder + csvs[0])
df = pd.read_csv(CSV_Folder + csvs[0])

G = Grapher.makeGraph(df)

Nodes = G.nodes()

print('remark' in Nodes)

N_list = []

for N in Nodes:
    N_list.append(N)

print(len(N_list))
