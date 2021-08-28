import numpy as np

mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(mat1)
mat2 = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
# print(mat2)


def alignDiagonally(M1, M2, prev_Len):
    for i in range(prev_Len, len(M1)):
        for j in range(prev_Len, len(M1)):
            M1[i][j] = M2[(i-prev_Len)][(j-prev_Len)]
    return M1


def resizeMatrix(M, I):
    oldMat_Len = len(M)
    appZero = len(I)
    zeros = np.zeros((appZero, appZero), dtype=np.int32)
    M = np.append(M, zeros, axis=1)
    L = np.zeros(len(M) + len(I))

    for i in range(len(I)):
        M = np.vstack((M, L))
    M = alignDiagonally(M, I, oldMat_Len)
    return M



print(resizeMatrix(mat1, mat2))
