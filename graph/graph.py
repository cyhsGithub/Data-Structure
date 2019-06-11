#用邻接矩阵，顶点从0开始计数
inf = float('inf')

class Graph:
    def __init__(self,mat,unconn=0):
        vnum = len(mat) #number of lines
        self.mat = [i[:] for i in mat]
        self.unconn = unconn
        self.vnum = vnum

    def vertex_num(self):
        return self.vnum

    def invalid(self,v):
        return v <0 or v >= self.vnum

    def add_edge(self,vi,vj,val=1):
        if self.invalid(vi) or self.invalid(vj):
            return False
        self.mat[vi][vj] = val

    def get_edge(self,vi,vj):
        if self.invalid(vi) or self.invalid(vj):
            return False
        return self.mat[vi][vj]

    def from_vertex(self,vi):
        if self.invalid(vi):
            return False
        return self.out(self.mat[vi],self.unconn)

    @staticmethod
    def out(row,unconn):
        edges = []
        for i,v in enumerate(row):
            if v != unconn:
                edges.append((i,v))
        return edges




