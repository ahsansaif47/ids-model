from keras.backend import print_tensor
from OCR_Post_processing import ocr_postprocessing
from keras.models import load_model
from spektral.layers import GCNConv
import pandas as pd
from Mat_Package import Grapher
import networkx as nx
import numpy as np
from gensim.models import Word2Vec

classifier = load_model("./Model/Model-0.3379.h5",
                        custom_objects={"GCNConv": GCNConv})

Emb_Model = "./Model/Word2Vec_Model.bin"
emb_model = Word2Vec.load(Emb_Model)


"""
1. Make Graph.
2. Make Adjacency Matrix.
3. Compute Embeddings.
4. Pass for prediction.
"""


def returnText(df):
    Text = []
    seenList = []
    text = df['Object'].to_list()

    for i in range(len(text)):
        if(text[i] not in seenList):
            Text.append(text[i])
        seenList.append(text[i])

    return Text


def computeEmbeddings(df):
    Text = returnText(df)
    _embeddings = []

    for t in Text:
        _embeddings.append(emb_model.wv[t])

    _embeddings = np.array(_embeddings)
    return _embeddings


def prediction():
    matrices = []
    Graphs = []
    pred = []
    # ocr_postprocessing.updation(ocr_postprocessing.big_G)
    print("= = = = = = = = = = = = = = =")
    for i in ocr_postprocessing.csvs:
        df = pd.read_csv(ocr_postprocessing.t_csv_folder + i)
        text = df['Object'].to_list()
        if 'remark' in text:
            print("Found in text")
        G = Grapher.makeGraph(df)
        ocr_postprocessing.big_G = nx.compose(ocr_postprocessing.big_G, G)
        ocr_postprocessing.update_GraphVocab(ocr_postprocessing.big_G)
        emb = computeEmbeddings(df)
        M = nx.to_numpy_array(G, dtype=np.int32)
        matrices.append(M)
        Graphs.append(G)
        l = classifier.predict_on_batch([emb, M])

    nx.write_gpickle(ocr_postprocessing.big_G, "./Graph DS/Graph.gpickle")
    # ocr_postprocessing.deleteFiles()
    # return pred


prediction()
# print(pred)
