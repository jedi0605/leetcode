class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        # print(graph)

        # doing DFS for Bob
        bob_time = {}  # node on root path -> time visited

        def dfs(src, pre, time):
            if src == 0:
                bob_time[src] = time
                return True
            for nei in graph[src]:
                if nei == pre:
                    continue
                if dfs(nei, src, time + 1):
                    bob_time[src] = time
                    return True
            return False

        dfs(bob, -1, 0)
        print(bob_time)
        # Alice BFS
        q = deque()
        q.append((0, 0, -1, amount[0]))  # node,time, pre, totoalProfit
        res = float("-inf")
        while q:
            node, time, pre, profit = q.popleft()
            for nie in graph[node]:
                if nie == pre:                    
                    continue
                nei_profit = amount[nie]
                nei_time = time + 1
                if nie in bob_time:
                    if nei_time > bob_time[nie]:
                        nei_profit = 0
                    if nei_time == bob_time[nie]:
                        nei_profit = nei_profit // 2
                q.append((nie, nei_time, node, profit + nei_profit))
                if len(graph[nie]) == 1:
                    res = max(res, profit+nei_profit)
        return res
