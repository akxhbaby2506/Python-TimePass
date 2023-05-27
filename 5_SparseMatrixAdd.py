matrix1 = {(0,2):1, (1,0):1, (2,1):1}
matrix2= {(0,0):1, (2,1):1}

matrix3={}

for key1 in matrix1.keys():
    if key1 in matrix2.keys():
        matrix3[key1] = matrix1[key1] + matrix2[key1]
    else:
        matrix3[key1] = matrix1[key1]

for key2 in matrix2.keys():
    if key2 in matrix1.keys():
        matrix3[key2] = matrix2[key2] + matrix1[key2]
    else:
        matrix3[key2]=matrix2[key2]

print(matrix3)