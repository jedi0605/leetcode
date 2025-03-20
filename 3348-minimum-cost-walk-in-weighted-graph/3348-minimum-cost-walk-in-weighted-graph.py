class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def union(self, x, y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p == y_p:
            return True
        if self.rank[x_p] > self.rank[y_p]:
            self.parent[y_p] = x_p
            self.rank[x_p] += 1
        else:
            self.parent[x_p] = y_p
            self.rank[y_p] += 1
        return True

    def find(self, x):
        while self.parent[x] != x:  # Keep moving up until we find the root
            # self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]  # Move x up one step
        return x


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        uf = UnionFind(n)
        for a, b, edge in edges:
            uf.union(a, b)
        componet_cost = {}
        for a, b, edge in edges:
            root = uf.find(a)
            if root not in componet_cost:
                componet_cost[root] = edge
            else:
                componet_cost[root] &= edge
        print(componet_cost)
        res = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(componet_cost[r1])
        return res
