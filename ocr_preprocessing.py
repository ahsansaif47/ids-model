import pandas as pd
import networkx as nx
from Mat_Package import Grapher
from gensim.models import Word2Vec
from Graph_DeepWalk import Graph_Deepwalk
import os

big_G = nx.read_gpickle("./Graph DS/Graph.gpickle")
t_csv_folder = "./Test Invoices Folder/CSVs/"

csvs = os.listdir(t_csv_folder)


def Make_Giant_Graph():
    Inc_Graph = nx.Graph()
    for i in range(len(csvs)):
        df = pd.read_csv(t_csv_folder+csvs[i])
        G = Grapher.makeGraph(df)
        Inc_Graph = nx.compose(Inc_Graph, G)

    return Inc_Graph


def Compose_and_Save_Graphs(G1, G2):
    G1 = nx.compose(G1, G2)
    nx.write_gpickle(G1, "./Graph DS/Graph.gpickle")


def update_GraphVocab(G):
    corpus = Graph_Deepwalk.build_deepwalk_corpus(G, num_paths=20)
    emb_model = Word2Vec(corpus, window=2, min_count=1, sg=1)
    emb_model.build_vocab(corpus)
    emb_model.train(corpus,
                    total_examples=len(corpus),
                    epochs=30,
                    report_delay=1)
    emb_model.save('./Model/Word2Vec_Model.bin')


def processing():
    pass


"""
Pre-Processing Pipeline:
1. Convert CSVs to Graph.
    1.1 Compose new CSVs Graphs.
2. Compose new Graph with already existing graph.
3. Save this newly created graph.
4. Update 

more than just one line
"""
