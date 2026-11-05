import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    n = len(A)
    m = len(A[0])
    M = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            M[j][i] = A[i][j]

    return np.array(M)
