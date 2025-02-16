class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, down = 0, len(matrix)
        res = []
        while left < right and top < down:
            # left 2 right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # top to down
            for i in range(top, down):
                res.append(matrix[i][right - 1])
            right -= 1
            if left >= right or top >= down:
                break
            # right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][i])
            down -= 1

            # down to top
            for i in range(down - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
