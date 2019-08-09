#用邻接表,顶点从0开始计数
from graph import Graph

class GraphAL(Graph):
    def __init__(self,Alist=[],mat=[],unconn=0):
        if Alist:
            vnum = len(Alist)
            self.mat = [i[:] for i in Alist]
        elif mat:
            self.mat = [Graph.out(i, unconn) for i in mat]
        else:
            return "Wrong parameters"

        self.vnum = vnum
        self.unconn = unconn

    def add_edge(self,vi,vj,val=1):
        if self.invalid(vi) or self.invalid(vj):
            return False

        row = self.mat[vi]
        for i, v in enumerate(row):
            if v[0] == vj:
                self.mat[vi][i] = (vj, val)
                return
        self.mat[vi].append((vj,val))

    def get_edge(self,vi,vj):
        if self.invalid(vi) or self.invalid(vj):
            return False

        for v,val in self.mat[vi]:
            if v == vj:
                return val

        return self.unconn

    def from_vertex(self,vi):
        if self.invalid(vi):
            return False
        return self.mat[vi]

# Alist = [[(2,6),(3,3)],
#          [(0,11),(2,4),(6,7)],
#          [(1,3),(4,5)],
#          [(4,5)],
#          [(5,9)],
#          [],
#          [(5,10)]]
# g = GraphAL(Alist)
# g.add_edge(2,5,1)
# e1 = g.get_edge(2,5)
# e2 = g.get_edge(0,5)
# v = g.from_vertex(6)
# print(e1,e2,v)
