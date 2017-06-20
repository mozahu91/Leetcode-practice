def rotate(A):
    A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
    A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
    return A   
