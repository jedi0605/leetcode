class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1 )
        print(dp)
        dp[0] = 0

        for i in range(1,amount + 1):
            for c in coins:
                # dp[1] -> using 1 coin
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
