#Kruskal algorithm
from AL import GraphAL

def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst,edges = [],[]

    for vi in range(vnum):
        for v,w in graph.from_vertex(vi):
            edges.append((w,vi,v))
    edges.sort() #sort by w

    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append(((vi,vj),w))
            if len (mst) == vnum - 1:
                break
            rep,orep = reps[vi],reps[vj]
            for i in range(vnum):#将与vj相连的结点的rep值全部改为和vi一样，这样所有连通的结点都是一个rep值
                if reps[i] == orep:
                    reps[i] = rep
    return mst

# 设G=（V，E）是一个网络，U是V的一个任意真子集，e为G的一条边，一个端点在U里，另一个不在，
# 而且e的权值与其他同情况的边相比最小，那么G必有一棵包括边e的最小生成树

#也需要联通量列表 判断两点是否连通
def prime(graph):
    vnum = graph.vertex_num()
    vertices = [0]
    mst = []
    cand = (vnum,float('inf'))
    candidate = []
    while len(mst) < vnum - 1:
        for vi in vertices:
            edges = graph.from_vertex(vi)
            if edges:
                for v,w in edges: #找出从vi出发的最近的未在生成树中的顶点
                    if v not in vertices:
                        if w < cand[1]:
                            cand = (v,w)
            v,w =  cand
            candidate.append((w,(vi,v)))
            cand = (vnum, float('inf'))
        candidate.sort()
        w,v = candidate[0]
        mst.append((v,w))
        vertices.append(v[1])
        candidate = []

    return mst


Alist = [[(2,6),(3,3)],
         [(0,11),(2,4),(6,7)],
         [(1,3),(4,5)],
         [(4,5)],
         [(5,9)],
         [],
         [(5,10)]]
# Alist = [[(1,5),(3,3)],
#          [],
#          [(1,4)],
#          [(2,6),(4,7)],
#          []]
g = GraphAL(Alist)
# tree = Kruskal(g)
tree = prime(g)
print(tree)

