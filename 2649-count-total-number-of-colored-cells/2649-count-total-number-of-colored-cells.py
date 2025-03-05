class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        times = 0
        for i in range(n):
            times+=i
        return 1+4*times