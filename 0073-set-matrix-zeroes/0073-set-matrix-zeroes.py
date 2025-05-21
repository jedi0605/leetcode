class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        init_arr = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    init_arr.append((r, c))

        def dfs(r, c, dir_r, dir_c):
            new_r = r + dir_r
            new_c = c + dir_c
            if 0 <= new_r < m and 0 <= new_c < n:
                matrix[new_r][new_c] = 0
                dfs(new_r, new_c, dir_r, dir_c)
            else:
                return

        dirt = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for r, c in init_arr:
            for dir_r, dir_c in dirt:
                # do dfs
                dfs(r, c, dir_r, dir_c)
        print(matrix)
