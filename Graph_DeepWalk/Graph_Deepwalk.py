import random
import networkx as nx
random.seed(666)


def random_walk(G, start=None, path_length=20, alpha=0, rand=random.Random()):
    '''return a random walk path'''
    if start:
        path = [start]
    else:
        path = [rand.choice(list(G.nodes()))]
    while len(path) < path_length:
        cur = path[-1]
        # find it's neighbors
        if len(G[cur]) > 0:
            if rand.random() >= alpha:
                path.append(rand.choice(list(nx.all_neighbors(G, cur))))
            else:
                path.append(path[0])
        else:
            break
    return path


def build_deepwalk_corpus(G, num_paths, rand=random.Random()):
    walks = []
    nodes = list(G.nodes())
    for i in range(num_paths):
        rand.shuffle(nodes)
        for node in nodes:
            walks.append(random_walk(G, start=node))
    return walks


# G = nx.read_gpickle('./Graph DS/Graph.gpickle')
# print(random_walk(G, start=None))
