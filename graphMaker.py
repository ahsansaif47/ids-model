from PIL.Image import Image
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from PIL import Image


csv = './A-10.csv'
df = pd.read_csv(csv)

xMIN = df['xmin']
xMAX = df['xmax']
yMIN = df['ymin']
yMAX = df['ymax']
Text = df['labels']


def findRight(df_ind):
    S_list = []
    xmax = xMAX[df_ind+1]
    ymin = yMIN[df_ind+1]
    ymax = yMAX[df_ind+1]

    for i in range(len(df)):
        if(xMIN[i] > xmax):
            if not (yMIN[i] > ymax or yMAX[i] < ymin):
                if(yMIN[i] <= ymin and yMAX[i] <= ymax):
                    S_list.append(i)
                elif (yMIN[i] <= ymin and yMAX[i] >= ymax):
                    S_list.append(i)
                elif (yMIN[i] >= ymin and yMAX[i] <= ymax):
                    S_list.append(i)
                elif (yMIN[i] >= ymin and yMAX[i] >= ymax):
                    S_list.append(i)
                elif (yMIN[i] == ymin and yMAX[i] == ymax):
                    S_list.append(i)

    print("Printing List")
    print(S_list)
    # print(df.head(S_list[0]))

    consec = 0
    for j in range(len(S_list)):
        for k in range(len(S_list)):
            print("XMAX[j]: ", xMAX[j])
            print("XMIN[k]: ", xMIN[k])
            # if(xMAX[j] < xMIN[k]):
            #     print("here")
            #     consec = S_list[j]

    return consec


def findLeft(df_ind):
    S_list = []
    xmin = xMIN[df_ind+1]
    ymin = yMIN[df_ind+1]
    ymax = yMAX[df_ind+1]

    for i in range(len(df)):
        if(xMAX[i] < xmin):
            if not (yMIN[i] > ymax or yMAX[i] < ymin):
                if(yMIN[i] <= ymin and yMAX[i] <= ymax):
                    S_list.append(i)
                elif (yMIN[i] <= ymin and yMAX[i] >= ymax):
                    S_list.append(i)
                elif (yMIN[i] >= ymin and yMAX[i] <= ymax):
                    S_list.append(i)
                elif (yMIN[i] >= ymin and yMAX[i] >= ymax):
                    S_list.append(i)
                elif (yMIN[i] == ymin and yMAX[i] == ymax):
                    S_list.append(i)

    return S_list


def findUp(df_ind):
    S_list = []
    xmin = xMIN[df_ind+1]
    xmax = xMAX[df_ind+1]
    ymin = yMIN[df_ind+1]

    for i in range(len(df)):
        if(yMAX[i] < ymin):
            if not (xMAX[i] < xmin or xMIN[i] > xmax):
                if(xMIN[i] <= xmin and xMAX[i] <= xmax):
                    S_list.append(i)
                elif (xMIN[i] <= xmin and xMAX[i] >= xmax):
                    S_list.append(i)
                elif (xMIN[i] >= xmin and xMAX[i] <= xmax):
                    S_list.append(i)
                elif (xMIN[i] >= xmin and xMAX[i] >= xmax):
                    S_list.append(i)
                elif (xMIN[i] == xmin and xMAX[i] == xmax):
                    S_list.append(i)

    return S_list


def findDown(df_ind):
    S_list = []
    xmin = xMIN[df_ind+1]
    xmax = xMAX[df_ind+1]
    ymax = yMAX[df_ind+1]

    for i in range(len(df)):
        if(yMIN[i] > ymax):
            if not (xMIN[i] < xmin or xMIN[i] > xmax):
                if(xMIN[i] <= xmin and xMAX[i] <= xmax):
                    S_list.append(i)
                elif (xMIN[i] <= xmin and xMAX[i] >= xmax):
                    S_list.append(i)
                elif (xMIN[i] >= xmin and xMAX[i] <= xmax):
                    S_list.append(i)
                elif (xMIN[i] >= xmin and xMAX[i] >= xmax):
                    S_list.append(i)
                elif (xMIN[i] == xmin and xMAX[i] == xmax):
                    S_list.append(i)

    return S_list


# for i in range(len(l)):
#     print(Text[l[i]])

G = nx.Graph()


def makeGraph():
    for i in range(len(df)):
        if findUp(i):
            l = findUp(i)
            text = ""
            for i in range(len(l)):
                text = Text[l[i]]
                G.add_edge(Text[i], text)
        if findRight(i):
            l = findRight(i)
            text = ""
            for i in range(len(l)):
                text = Text[l[i]]
                G.add_edge(Text[i], text)
            # G.add_edge(Text[i], findRight(i))
        if findDown(i):
            l = findDown(i)
            text = ""
            for i in range(len(l)):
                text = Text[l[i]]
                G.add_edge(Text[i], text)
            # G.add_edge(Text[i], findDown(i))
        if findLeft(i):
            l = findLeft(i)
            text = ""
            for i in range(len(l)):
                text = Text[l[i]]
                G.add_edge(Text[i], text)
            # G.add_edge(Text[i], findLeft(i))

    nx.draw_shell(G, with_labels=True)
    plt.savefig("InvoiceGraph.png")


# makeGraph()

print(df.head(8))
# print()

x = findRight(3)
print(x)

# adj_Mat = nx.adjacency_matrix(G)
# print(adj_Mat.todense())
