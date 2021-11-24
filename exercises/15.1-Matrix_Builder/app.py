import random

#Create the function below:
def matrixBuilder(integer):
    matrix = []
    for i in range(integer):
        
        matrix.append([])
        for x in range(integer):
            matrix[i].append(1)

    return matrix

print(matrixBuilder(random.randint(1, 9)))