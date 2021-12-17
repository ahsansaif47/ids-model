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


def computeEmbeddings(Text):
    _embeddings = []

    for t in Text:
        _embeddings.append(emb_model.wv[t])

    _embeddings = np.array(_embeddings)
    return _embeddings


data = {
    0: 'Shipping Address',
    1: 'Billing Info',
    2: 'Product Description',
    3: 'Product Description',
    4: 'Invoice Details',
    5: 'Issuer Address',
    6: 'Nan',
    7: 'Note',
    8: 'Product Net',
    9: 'Product Price',
    10: 'Quantity',
    11: 'Shipping Address',
}


def prediction():
    matrices = []
    Graphs = []
    pred = []
    for i in ocr_postprocessing.csvs:
        df = pd.read_csv(ocr_postprocessing.t_csv_folder + i)
        text = returnText(df)
        G = Grapher.makeGraph(df)
        ocr_postprocessing.big_G = nx.compose(ocr_postprocessing.big_G, G)
        ocr_postprocessing.update_GraphVocab(ocr_postprocessing.big_G)
        emb = computeEmbeddings(text)
        emb = emb[0:len(emb)-1]
        M = nx.to_numpy_array(G, dtype=np.int32)
        matrices.append(M)
        Graphs.append(G)
        pr = classifier.predict_on_batch([emb, M])
        prediction = np.argmax(pr, axis=1)
        # print(prediction)
        i = 0
        for p in prediction:
            print(text[i], " is: ", data[p])
            i += 1

    nx.write_gpickle(ocr_postprocessing.big_G, "./Graph DS/Graph.gpickle")
    # ocr_postprocessing.deleteFiles()
    # return pred


prediction()
# predictions = np.argmax(predictions, axis=1)
