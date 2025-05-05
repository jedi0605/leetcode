class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        print(53 % MOD)
        if n == 1: return 1
        dp = [1] *(n+1)
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]*2 + dp[i-3]
            dp[i] = dp[i] % MOD            
        return dp[n]