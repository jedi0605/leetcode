class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        dirct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:  # count
                    # Check 4 dirct
                    for d_r, d_c in dirct:
                        new_row, new_col = r + d_r, c + d_c
                        if (
                            0 <= new_row < ROW
                            and 0 <= new_col < COL
                            and grid[new_row][new_col] == 0
                        ):
                            res += 1
                        if new_row < 0 or new_row == ROW:
                            res += 1
                        if new_col < 0 or new_col == COL:
                            res += 1

        return res
