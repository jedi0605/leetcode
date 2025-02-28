class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        maps = defaultdict(list)
        for e1, e2 in edges:
            maps[e1].append(e2)
            maps[e2].append(e1)
        bob_time = {}  # node, time
        tmp = []

        def dfs(src, pre, time):
            if src == 0:
                bob_time[src] = time
                return True
            for nei in maps[src]:
                if nei == pre:
                    continue
                if dfs(nei, src, time + 1):
                    bob_time[src] = time
                    return True
            return False

        dfs(bob, -1, 0)
        print(bob_time)
        res = float("-inf")
        q = deque()
        q.append((0, 0, -1, amount[0]))  # curNode, time, preNode, totalProfit
        while q:
            curN, time, preN, totalP = q.popleft()
            for nie in maps[curN]:
                if nie == preN:
                    continue
                nie_profit = amount[nie]
                nie_time = time + 1
                if nie in bob_time:
                    if nie_time > bob_time[nie]:
                        nie_profit = 0
                    if nie_time == bob_time[nie]:
                        nie_profit = nie_profit // 2
                q.append((nie, nie_time, curN, totalP + nie_profit))
                if len(maps[nie]) == 1:
                    res = max(res, totalP + nie_profit)
        return res
