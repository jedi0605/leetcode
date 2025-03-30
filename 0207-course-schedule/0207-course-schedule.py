class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # maps:
        # a :
        # b : 
        # c : 
        # d :
        maps = defaultdict(set)
        for c, pre in prerequisites:
            maps[c].add(pre)
        print(maps)

        def dfs(n):
            if len(maps[n]) == 0:
                return True
            if n in visited:
                return False
            visited.add(n)
            for nei in maps[n]:
                if dfs(nei) == False:
                    return False
            maps[n] = set()
            return True
        
        for n in range(numCourses):
            visited = set()    
            if dfs(n) == False:
                return False
        return True