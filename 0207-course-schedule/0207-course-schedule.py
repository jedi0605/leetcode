class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur] == []:
                return True

            visited.add(cur)
            for crs in preMap[cur]:
                if dfs(crs) == False:
                    return False
            visited.remove(cur)
            preMap[cur] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True

