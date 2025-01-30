class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        res = []
        queue = deque()
        for i in range(len(mat)):
            res.append([])
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    res[i].append(0)
                    visited.add((i, j))
                    queue.append([i, j])
                else:
                    res[i].append(float("inf"))

        while queue:
            for _ in range(len(queue)):
                c_r, c_c = queue.popleft()
                for x, y in direc:
                    if (
                        0 <= c_r + x < len(mat)
                        and 0 <= c_c + y < len(mat[0])
                        and (c_r + x, c_c + y) not in visited
                    ):
                        visited.add((c_r + x, c_c + y))
                        res[c_r + x][c_c + y] = res[c_r][c_c] + 1
                        queue.append([c_r + x, c_c + y])
        return res
