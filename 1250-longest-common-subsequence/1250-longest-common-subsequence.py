class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text2) + 1
        col = len(text1) + 1
        dp = [[0] * col for i in range(row)]
        for r in range(1, row):
            for c in range(1, col):
                if text2[r - 1] == text1[c - 1]:
                    dp[r][c] = dp[r - 1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]
