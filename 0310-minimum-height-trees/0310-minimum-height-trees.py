class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        maps = defaultdict(set)
        for a,b in edges:
            maps[a].add(b)
            maps[b].add(a)
        leave = []
        for key, vals in maps.items():
            if len(vals) == 1:
                leave.append(key)
        
        while n>2:
            n -= len(leave)
            new_leave = []
            for cur in leave:
                l = maps[cur].pop()
                maps[l].remove(cur)
                if len(maps[l]) == 1:
                    new_leave.append(l)
            leave = new_leave
        return list(leave)