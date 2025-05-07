class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maps = defaultdict(list) # node -> prob,nei_node
        for i in range(len(edges)):
            a,b = edges[i][0], edges[i][1]
            maps[a].append((succProb[i],b))
            maps[b].append((succProb[i],a))
        max_heap = [(-1,start_node)]
        visited = set()
        while max_heap:
            cur_prob, node = heappop(max_heap)
            cur_prob = cur_prob * -1
            visited.add(node)
            if node == end_node: return cur_prob
            
            for nei_prob,nei in maps[node]:
                if nei not in visited:
                    new_prob = nei_prob * cur_prob * -1
                    heappush(max_heap, (new_prob,nei))
        return 0
