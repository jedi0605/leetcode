class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp =[]
        dp = [[0  for _ in range(len(matrix[0]))]  for _ in range(len(matrix))  ]
        
        res = 0
        for i in range(len(matrix)):            
            dp[i][0] = matrix[i][0]
            res += dp[i][0]
        
        for i in range(1,len(matrix[0])):            
            dp[0][i] = matrix[0][i]
            res+=dp[0][i]
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] =min( dp[i-1][j-1] , dp[i][j-1], dp[i-1][j]) +1
                res += dp[i][j]
        return res