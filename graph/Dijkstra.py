from graph import Graph

def dijkstra(graph,v0):
    vnum = graph.vertex_num()
    edges = graph.from_vertex(v0)
    mat = graph.get_mat()
    # changes = [[]] * vnum #这样写的话，里面[]的地址都一样，改一个都改了
    changes = [[] for i in range(vnum)]
    nearest = []
    path = []
    vertices = [v0]
    for i in range(vnum-1):
        for v,w in edges:
            if v not in vertices:
                nearest.append((w,v))
        #找到从v0出发的一条最短路径
        nearest.sort()
        #如果从v0出发没有路了，则把v0到所有其他点的距离设为inf，即原本的距离
        if nearest == []:
            for n in range(vnum):
                if n not in vertices:
                    path.append(((v0, n), mat[v0][n]))
            return path
        #v0到v的路径是剩余点中最短的
        w,v = nearest[0]
        nearest = []

        #如果v0到v中间没有其他点，则按照else，否则按照if，将最短路径加入path
        if changes[v] != []:
            path.append(((v0, changes[v],v), w))
        else:
            path.append(((v0,v),w))
        vertices.append(v)

        #更新从v0经过v到其他点的距离，如果比原来短，则替换，记录中间点
        for vertice in range(vnum):
            if vertice not in vertices:
                update = mat[v0][v] + mat[v][vertice]
                if mat[v0][vertice] > update:
                    mat[v0][vertice] = update

        #更新邻接矩阵
        graph.update_mat(mat)
        edges = graph.from_vertex(v0)

    return path

inf = float("inf")
mat = [[0,5,inf,3,inf],
       [inf,0,inf,inf,inf],
       [inf,4,0,inf,inf],
       [inf,inf,6,0,7],
       [inf,inf,inf,inf,0]]
g = Graph(mat,unconn=inf)
path = dijkstra(g,2)
print(path)



