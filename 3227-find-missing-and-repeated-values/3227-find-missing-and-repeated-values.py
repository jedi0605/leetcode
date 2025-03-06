class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        arr = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                arr[grid[i][j] - 1] += 1
        miss = 0
        repeat = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                miss = i + 1
            if arr[i] == 2:
                repeat = i + 1
        return [repeat, miss]
