class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0] 
            b = questions[i][1] 
                        
            if i + b + 1 < n:
                dp[i] += dp[i + b+1]
            dp[i] = max(dp[i], dp[i+1])            
        return dp[0]
