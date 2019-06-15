#无权图的最短路径由广度优先遍历求解
from graph import Graph

def floyd(graph,v):
    vnum = graph.vertex_num()
    e = graph.get_mat()
    for k in range(vnum): #以第k个点为中转站
        for i in range(vnum):
            for j in range(vnum):
                update = e[i][k] + e[k][j]
                if e[i][j] > update:
                    e[i][j] = update
    return e[v]

inf = float("inf")
mat = [[0,5,inf,3,inf],
       [inf,0,inf,inf,inf],
       [inf,4,0,inf,inf],
       [inf,inf,6,0,7],
       [inf,inf,inf,inf,0]]
g = Graph(mat)
path = floyd(g,0)
print(path)