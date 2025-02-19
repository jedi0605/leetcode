class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while top <= down and left <= right:
            # left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # top to down
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left >= right+1 or top >= down+1:
                break
            # right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1

            # down to top
            for i in range(down, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
