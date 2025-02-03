class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = []
        for c, pre in prerequisites:
            courseMap[c].append(pre)

        visited = set()

        def dfs(course):
            if courseMap[course] == []:
                return True

            if course in visited:
                return False
            visited.add(course)

            for cou in courseMap[course]:
                if dfs(cou) == False:
                    return False
            visited.remove(course)
            courseMap[course] = []
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
