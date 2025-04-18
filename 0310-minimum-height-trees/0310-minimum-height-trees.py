class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        height = [float("inf")] * n
        if n == 1:
            return [0]
        graph = defaultdict(set)  # connection, 0->1,   1-> 0,2,3 ....
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = []
        for src, l in graph.items():
            if len(l) == 1:
                leaves.append(src)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                nei = graph[l].pop()
                graph[nei].remove(l)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        return list(leaves)
