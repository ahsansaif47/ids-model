import numpy as np
import networkx as nx


def nodeFeatures(A):
    # X = Features Matrix
    X = np.matrix([[i, -i] for i in range(A.shape[0])], dtype=float)
    print("Printing Feature Matrix..")
    print(X)

    # Identity matrix of the same shape as adjacency matrix
    I = np.matrix(np.eye(A.shape[0]))

    # Self looping making node connections with themselves
    # i.e. multiply the adjacency matrix with identity matrix
    A_new = A + I

    # Multiplying the self-looped graph with the feature matrix

    # Stores the sum of array(Row wise) in a new array called D
    D = np.array(np.sum(A, axis=0))[0]

    # Making the diagonal matrix named D containing the elements of 1D array D
    # D = np.matrix(np.diag(D))
    # print("Printing the 2D array named D containing the elemnets of 1D D in diagonal")
    # print(D)

    # Stores the degree of the graph in a 1D array called D
    D = np.array(np.sum(A_new, axis=0))[0]
    # Transforming that 1D array to a degree matrix
    D = np.matrix(np.diag(D))
    # print("Degree matrix of A_new multiplied by A_new..")
    D_new = D * A_new
    # print(D_new)

    # Weight Matrix
    W0 = np.random.randn(X.shape[1], 8) * 0.01

    print("Printing Weights")
    print(W0)

    # Reducing feature of output feature representation..
    print("Output feature representation..")
    final = D_new**-1 * A_new * X * W0

    def relu(x):
        return np.maximum(0, x)

    H_1 = relu(final)
    # print("After applying relu function..")
    # print(H_1)

    output = H_1

    # print("Printing A_new matrix..")
    # print(A_new)

    G = nx.from_numpy_matrix(np.array(A_new))
    # nx.draw_networkx_edges(G, pos=nx.spring_layout(
    #     G), arrowstyle="<|-", style="dashed")
    # plt.show()
    # nx.draw(G)
    # plt.savefig("/content/Sample Graph.png")
    feature_representations = {
        node: np.array(output)[node]
        for node in G.nodes()
    }

    features = np.array(feature_representations.values())

    # print("Printing feature representation..")
    # print(features)

    vals = []

    for v in feature_representations.values():
        vals.append(v)

    vals = np.array(vals)

    # print("Prining features in an array", vals)

    # print("Shape of vals is: ", np.shape(vals))

    return vals
