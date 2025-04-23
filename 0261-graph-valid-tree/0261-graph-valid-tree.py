class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        maps = defaultdict(list)

        for a, b in edges:
            maps[a].append(b)
            maps[b].append(a)
        visited = set()

        def dfs(pre, cur):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in maps[cur]:
                if nei == pre:
                    continue
                if not dfs(cur, nei):
                    return False
            return True

        res = dfs(None, 0)
        if len(visited) != n:
            return False
        return res

        # build maps
        # maps = defaultdict(list)

        # for a, b in edges:
        #     maps[a].append(b)
        #     maps[b].append(a)
        # print(maps)
        # queue = deque()
        # queue.append(0)
        # # If add 1, will lost some edge case like [1,0] [2,3]
        # # for key, val in maps.items():
        # #     if len(val) == 1:
        # #         queue.append(key)
        # visited = set()
        # parent = {}
        # while queue:
        #     cur = queue.popleft()
        #     visited.add(cur)
        #     for nei in maps[cur]:
        #         if parent.get(cur) == nei:
        #             continue
        #         if nei in visited:
        #             return False
        #         parent[nei] = cur
        #         queue.append(nei)
        # return len(visited) == n
