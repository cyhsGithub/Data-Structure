mat = [[1,2,3],
       [4,5,6]]

res = [[0 for i in range(len(mat))] for n in range(len(mat[0]))]

for i in range(len(res)):
    for j in range(len(res[0])):
        res[i][j] = mat[j][i]

print(res)