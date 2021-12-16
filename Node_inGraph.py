import networkx as nx

bG = nx.read_gpickle("./Graph DS/Graph.gpickle")

if 'date' in bG:
    print("Present in Graph..")

else:
    print("Not in Graph")
