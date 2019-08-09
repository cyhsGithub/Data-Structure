m = 20
n = 4
x = [0,6,7,12,14]
r = [0,5,6,5,1]
opt = [0 for i in range(n)]
e = [0 for i in range(n)]

for i in range(1, n):
    for j in range(i,-1,-1):
        if x[i] - x[j] > 5:
            e[i] = j
            break

for i in range(1, n):
    opt[i] = max(opt[i-1], opt[e[i]] + r[i])

print(max(opt))