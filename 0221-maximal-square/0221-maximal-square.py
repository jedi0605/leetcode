class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_q = 0
        print(dp)        

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c])
                    max_q = max(dp[r][c], max_q)        

        return max_q * max_q
