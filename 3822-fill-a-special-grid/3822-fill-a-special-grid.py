class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        val = 0
        size = 2**n
        grid = [[0] * size for _ in range(size)]

        def dfs(rowStart, rowEnd, colStart, colEnd):
            nonlocal grid, val
            sz = rowEnd - rowStart
            if sz == 1:
                # print(f"{rowStart},{colStart}")
                grid[rowStart][colStart] = val
                val += 1
                return
            next_r = rowStart + sz // 2
            next_c = colStart + sz // 2
            # go to top right
            dfs(rowStart, next_r, next_c, colEnd)
            dfs(next_r, rowEnd, next_c, colEnd)
            dfs(next_r, rowEnd, colStart, next_c)
            dfs(rowStart, next_r, colStart, next_c)

        dfs(0, size, 0, size)
        # print(grid)
        return grid
