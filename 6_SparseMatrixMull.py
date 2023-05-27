matrix1 = [[0,2,0],[0,0,1],[7,0,0]]
matrix2 = [[4,0,8],[0,3,0],[0,0,6]]
matrix3 = []

for i in range(3):
    for j in range(3):
        sum = 0
        for k in range(3):
            sum = sum + (matrix1[i][k] * matrix2[j][k])
        matrix3[i].append(sum)

print(matrix3)
