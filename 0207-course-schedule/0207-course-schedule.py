class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = defaultdict(set)
        for course, pre in prerequisites:
            maps[pre].add(course)
        visited = set()

        def dfs(start):
            if len(maps[start]) == 0:
                return True
            if start in visited:
                return False
                
            visited.add(start)
            for c in maps[start]:
                if dfs(c) == False:
                    return False
            visited.remove(start)
            maps[start] = set()
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
