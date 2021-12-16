import pandas as pd
import networkx as nx
from Mat_Package import Grapher
from gensim.models import Word2Vec
from Graph_DeepWalk import Graph_Deepwalk
import os

big_G = nx.read_gpickle("./Graph DS/Graph.gpickle")
t_csv_folder = "./Test Invoices Folder/CSVs/"

csvs = os.listdir(t_csv_folder)

"""
Pre-Processing Pipeline:
1. Convert CSVs to Graph.
    1.1 Compose new CSVs Graphs.
2. Compose new Graph with already existing graph.
3. Save this newly created graph.
4. Update Embeddings model vocabulary.
5. Save embeddings model.
6. Delete CSV Files.
"""


def Save_Graphs(G):
    nx.write_gpickle(G, "./Graph DS/Graph.gpickle")


def update_GraphVocab(G):
    print("= = = = = = = = = = = = = = =")
    print("Updating Emb Model Vocab..")
    print("= = = = = = = = = = = = = = =")
    corpus = Graph_Deepwalk.build_deepwalk_corpus(G, num_paths=20)
    emb_model = Word2Vec(corpus, window=2, min_count=1, sg=1)
    emb_model.build_vocab(corpus)
    emb_model.train(corpus,
                    total_examples=len(corpus),
                    epochs=30,
                    report_delay=1)
    emb_model.save('./Model/Word2Vec_Model.bin')


def deleteFiles():
    for i in csvs:
        os.remove(t_csv_folder+i)
