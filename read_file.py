import numpy as np

def create_matrix_c(filename):
    with open(filename, 'r') as infile:
        shapeA = [int(num) for num in infile.readline().split()]
        shapeB = [int(num) for num in infile.readline().split()]
        matrixA = np.array([int(num) for row in range(shapeA[0]) for num in infile.readline().split()]).reshape(shapeA[0], -1)
        # matrixA = np.array([[int(num) for num in infile.readline().split()] for _ in range(shapeA[0])])
        matrixB = np.array([int(num) for row in range(shapeB[0]) for num in infile.readline().split()]).reshape(shapeB[0], -1)
        # matrixB = np.array([[int(num) for num in infile.readline().split()] for _ in range(shapeB[0])])

    # print(shapeA)
    # print(shapeB)
    print(matrixA)
    print(matrixB)

    matrixC = np.copy(matrixB)
    for i in range(shapeA[0]):
        for j in range(shapeA[1]):
            if matrixA[i, j] < matrixB[i + shapeB[0] - shapeA[0], j + shapeB[1] - shapeA[1]]:
                matrixC[i + shapeB[0] - shapeA[0], j + shapeB[1] - shapeA[1]] = 0
            else:
                matrixC[i + shapeB[0] - shapeA[0], j + shapeB[1] - shapeA[1]] = 1
    return matrixC

if __name__ == "__main__":
    file = './test.txt'
    print(create_matrix_c(file))