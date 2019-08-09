m = [389,207,155,300,299,170,158,65]
a = [0 for i in range(len(m))]

for i in range(len(a)):
    index = []
    for n in range(i):
        if m[n] > m[i]:
            index.append(n)
    if index == []:
        a[i] = 1
    else:
        a[i] = max(a[p]+1 for p in index)

print(a[-1])