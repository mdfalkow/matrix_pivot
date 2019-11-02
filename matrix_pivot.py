import numpy as np


def pivot(A: np.ndarray, ip: int, jp: int):
    """
    Performs a pivot operation on the matrix A using A[ip, jp] as the pivot 
    element. Treats M as a matrix of floats.

    Parameters
    ---------- 
    A : numpy.ndarray
        2D matrix on which pivot operation will be performed
    ip : int 
        row of pivot element
    jp : int 
        column of pivot element

    Returns
    -------
    numpy.ndarray
        the matrix A after the pivot on A[ip, jp] has been performed.
    """

    assert isinstance(A, np.ndarray)
    assert len(A.shape) == 2
    if A[ip, jp] == 0:
        return
    else:
        A_new = np.array(A)
        for i in range(0, A.shape[0]):
            if i != ip:
                A_new[i, :] = A[i, :] - A[ip, :] * (A[i, jp] / A[ip, jp])
            else:
                A_new[i, :] = A[i, :] / A[ip, jp]

    return A_new
