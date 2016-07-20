class ShapeError(Exception):
    pass

def shape(vector):
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    rows = len(vector)
    if isinstance(vector[0], list):
        cols = len(vector[0])
        return (rows, cols)
    else:
        return (rows,)

def vector_add(vector_a, vector_b):
    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    if shape(vector_a) == shape(vector_b):
        return ([val_a + val_b for val_a, val_b in zip(vector_a, vector_b)])
    else:
        raise ShapeError("Vectors are of different lengths")


def vector_sub(vector_a, vector_b):
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    """
    if shape(vector_a) == shape(vector_b):
        return ([val_a - val_b for val_a, val_b in zip(vector_a, vector_b)])
    else:
        raise ShapeError("Vectors are of different lengths")


def vector_sum(*args):
    length = len(args[0])
    # Ensure all arguments are at the same length without a loop:
    # There's gotta be a more efficient way to do this w/o using a loop
    same_len_args = [arg for arg in args if len(arg) == length]
    if len(same_len_args) == len(args):
        return [sum(arg) for arg in zip(args)]   ################################  NEED HELP HERE
    else:
        raise ShapeError("Vectors must be the same size")

def dot(vector_a, vector_b):
    if shape(vector_a) == shape(vector_b):
        return sum([val_a * val_b for val_a, val_b in zip(vector_a, vector_b)])
    else:
        raise ShapeError("Vectors must be the same size")

def vector_multiply(vector, number):
    return [val * number for val in vector]

def vector_mean(vector_a, vector_b):
    return [(val_a + val_b) / 2 for val_a, val_b in zip(vector_a, vector_b)]

def magnitude(vector):
    return sum([val ** 2 for val in vector]) ** 0.5

def matrix_row(matrix, row):
    return matrix[row]

def matrix_col(matrix, row):
    return [vector[row] for vector in matrix]

def matrix_add(matrix_a, matrix_b):
    if shape(matrix_a) == shape(matrix_b):
        return [vector_add(vector_a, vector_b) for vector_a, vector_b in zip(matrix_a, matrix_b)]
    else:
        raise ShapeError("Matrices must be the same size")

def matrix_sub(matrix_a, matrix_b):
    if shape(matrix_a) == shape(matrix_b):
        return [vector_sub(vector_a, vector_b) for vector_a, vector_b in zip(matrix_a, matrix_b)]
    else:
        raise ShapeError("Matrices must be the same size")


A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
C = [[1, 2],
     [2, 1],
     [1, 2]]
D = [[1, 2, 3],
     [3, 2, 1]]

m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]




def main():
    pass

if __name__ == '__main__':
    main()
