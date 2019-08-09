Alist = [[(1,4),(2,2),(3,3)],
         [(4,9),(5,8)],
         [(4,6),(5,7),(6,8)],
         [(5,4),(6,7)],
         [(7,5),(8,6)],
         [(7,8),(8,6)],
         [(7,6),(8,5)],
         [(9,7)],
         [(9,3)],
         []]

path = []
cost = [10 for i in range(10)]
# cost[7] = 7
# cost[8] = 3
cost[9] = 0

for i in range(8, -1, -1):
    c = []
    for v, w in Alist[i]:
        c.append(cost[v] + w)
    cost[i] = min(c)
    index = c.index(min(c))
    node = Alist[i][index][0]
    path.append(node)

final_path = [0]
i = 0
path = path[::-1]
while path[i] is not 9:
    final_path.append(path[i])
    i = path[i]

final_path.append(9)

print(final_path)
print(cost[0])
        



