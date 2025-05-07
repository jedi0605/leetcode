class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maps = defaultdict(list) # node, nei
        for i in range(len(edges)):
            a,b = edges[i][0],edges[i][1]
            maps[a].append( (b ,succProb[i]))
            maps[b].append((a,succProb[i]))
        max_heap = [(-1,start_node)]
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        while max_heap:
            cur_prob, node = heappop(max_heap)
            cur_prob = -1 * cur_prob
            if node == end_node:
                return cur_prob
            for nei, prob in maps[node]:
                new_prob = cur_prob * prob
                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob
                    heappush(max_heap, (-new_prob,nei))
        return 0
        