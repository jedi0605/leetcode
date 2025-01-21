class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        res = [[float("inf")] * col for _ in range(row)]
        diretion = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        print(res)
        visited = set()
        queue = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    visited.add((r, c))
                    queue.append((r, c, 0))

        while queue:
            cur_r, cur_c, dist = queue.popleft()
            for d_r, d_c in diretion:
                new_r, new_c = cur_r + d_r, cur_c + d_c
                if new_r < 0 or new_r == row or new_c < 0 or new_c == col:
                    continue
                if (new_r, new_c) in visited:
                    continue
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist+1))
                res[new_r][new_c] = dist+1
        return res
