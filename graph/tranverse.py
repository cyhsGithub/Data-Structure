from AL import GraphAL
from LStack import LStack
from LQueue import Queue

def DFS_tranverse(graph,v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 0
    DFS_seq = [v0]

    st = LStack()
    st.push((0,graph.from_vertex(v0)))
    while not st.is_empty():
        i,edges = st.pop()
        if i < len(edges):
            v,e = edges[i]
            st.push((i+1,edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0,graph.from_vertex(v)))
    return DFS_seq

def WFS_tranverse(graph,v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = [0] * vnum
    WFS_seq = [v0]

    qu = Queue()
    qu.enqueue((0,graph.from_vertex(v0)))
    while not qu.is_empty():
        i,edges = qu.dequeue()
        if i < len(edges):
            qu.enqueue((i+1,edges))
            v,w = edges[i]
            if not visited[v]:
                WFS_seq.append(v)
                visited[v] = 1
                qu.enqueue((0,graph.from_vertex(v)))
    return WFS_seq

Alist = [[(2,6),(3,3)],
         [(0,11),(2,4),(6,7)],
         [(1,3),(4,5)],
         [(4,5)],
         [(5,9)],
         [],
         [(5,10)]]
g = GraphAL(Alist)
d = DFS_tranverse(g,0)
w = WFS_tranverse(g,0)
print(d,w)

