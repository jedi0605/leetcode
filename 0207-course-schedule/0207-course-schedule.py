class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = defaultdict(list)
        for cour, pre in prerequisites:
            maps[cour].append(pre)
        print(maps)
        visited = set()

        def have_cyc(c):
            if len(maps[c]) == 0:
                return False
            if c in visited:
                return True
            visited.add(c)
            for nie in maps[c]:
                if have_cyc(nie):
                    return True
            visited.remove(c)
            return False

        for i in range(numCourses):
            if have_cyc(i):
                return False
        return True
