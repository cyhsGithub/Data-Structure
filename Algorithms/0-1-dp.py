w = [2,2,6,5,4]
v = [6,3,5,4,6]
C = 10
tab = [[0 for i in range(C+1)] for n in range(len(w)+1)]

for i in range(1,len(tab)):
    for j in range(1, len(tab[i])):
        tab[i][j] = tab[i-1][j] if j<w[i-1] else max(tab[i-1][j], tab[i-1][j-w[i-1]]+v[i-1])

print(tab[-1][-1])
