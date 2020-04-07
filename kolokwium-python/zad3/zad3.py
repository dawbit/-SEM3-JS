def Transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])

        f = open("macierzwynikowa.txt","w")
    for r in transposed:
        f.write(str(r)+'\n')

matrix = []
with open("macierzwejsciowa.txt", "r") as f:
    contents = f.read().split('\n')

    for element in contents:
        matrix.append(element.split())

    Transpose(matrix)

