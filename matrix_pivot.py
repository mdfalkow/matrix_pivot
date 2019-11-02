import numpy as np


def pivot(A: np.array, ip, jp):
    if A[ip, jp] != 0:
        A_new = np.array(A)
        for i in range(0, A.shape[0]):
            if i != ip:
                A_new[i, :] = A[i, :] - A[ip, :] * (A[i, jp] / A[ip, jp])
            else:
                A_new[i, :] = A[i, :] / A[ip, jp]

    return A_new
