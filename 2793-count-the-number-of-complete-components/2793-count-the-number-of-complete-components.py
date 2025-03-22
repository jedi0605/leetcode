class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.Size = [1] * N

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # path compression
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x == y:
            return False

        if self.Size[x] > self.Size[y]:
            self.Size[x] += self.Size[y]
            self.root[y] = x
        else:
            self.Size[y] += self.Size[x]
            self.root[x] = y
        return True


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        for x, y in edges:
            uf.Union(x, y)
        comp_size = [0] * n
        comp_edge = [0] * n
        for i in range(n):
            comp_size[uf.Find(i)] += 1
        for x, y in edges:
            comp_edge[uf.Find(x)] += 1
        print(comp_size)
        print(comp_edge)
        count = 0
        for i in range(n):
            if uf.Find(i) == i: # means is root
                if comp_edge[i] == (uf.Size[i] * (uf.Size[i]-1) / 2):
                    count+=1
        return count