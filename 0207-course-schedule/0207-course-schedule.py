class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        print(preMap)
        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur] == []:
                return True
            visited.add(cur)
            for num in preMap[cur]:
                if dfs(num) == False:
                    return False                    
            visited.remove(cur)
            preMap[cur] = []        
            return True
        
        for n in range(numCourses):
            if dfs(n) == False:
                return False                    
        return True