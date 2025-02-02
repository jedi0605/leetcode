class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()
        for c in range(len(prerequisites)):
            preMap[prerequisites[c][0]].append(prerequisites[c][1])
        print(preMap)
        
        def dfs(crs):
            if crs in visited:
                return False

            if len(preMap[crs]) == 0:
                return True
            visited.add(crs)

            for c in preMap[crs]:
                if dfs(c) == False:
                    return False
            preMap[crs] = []
            visited.remove(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
