class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_q = 0

        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            max_q = max(max_q, dp[0][i])

        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            max_q = max(max_q, dp[i][0])

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != "0":
                    dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c])
                    max_q = max(dp[r][c], max_q)
        print(dp)

        return max_q * max_q
