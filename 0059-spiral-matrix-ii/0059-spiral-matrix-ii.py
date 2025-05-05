class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        start = 1

        up_row = 0
        down_row = n - 1
        left_col = 0
        right_col = n - 1
        while start <= n**n:
            if up_row == down_row:
                res[up_row][left_col] = start
                break
            if start > n*n:
                break
            for i in range(left_col, right_col + 1):
                res[up_row][i] = start
                start += 1
            up_row += 1

            for i in range(up_row, down_row + 1):
                res[i][right_col] = start
                start += 1
            right_col -= 1

            for i in range(right_col, left_col - 1, -1):
                res[down_row][i] = start
                start += 1
            down_row -= 1

            for i in range(down_row, up_row - 1, -1):
                res[i][left_col] = start
                start += 1
            left_col += 1
            print(res)
        return res
