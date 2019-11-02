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

    # Check if pivot element is 0
    if A[ip, jp] == 0:
        return

    M = np.asfarray(A) # convert to float array
    M_new = np.array(M)
    for i in range(0, M.shape[0]):
        if i != ip:
            M_new[i, :] = M[i, :] - M[ip, :] * (M[i, jp] / M[ip, jp])
        else:
            M_new[i, :] = M[i, :] / M[ip, jp]

    return M_new
