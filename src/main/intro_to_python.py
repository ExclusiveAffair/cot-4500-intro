import numpy as np

# returns the dim x dim identity matrix containing 32-bit integers
def gen_identity(dim):
    return np.identity(dim, dtype = np.dtype(np.int32))

# prints space-separated rows and columns of the given matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()
    print()
            
N = 3

if __name__ == "__main__":
    
    # step 1: set matrix[i][j] to 1 iff i == j
    
    matrix = gen_identity(N)
    print_matrix(matrix)

    # step 2: increment matrix[i][j] by 3 iff i != j
 
    matrix += (1 - matrix) * 3
    print_matrix(matrix)

    # step 3: delete the last column of the matrix

    matrix = np.delete(matrix, N - 1, 1)
    print_matrix(matrix)
