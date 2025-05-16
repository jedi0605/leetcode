class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        prev = [-1] *n
        dp = [1] * n
        max_len , end_idx = 1,0
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if groups[i] != groups[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    prev[i] = j
        max_idx = dp.index(max(dp))

        res = []

        while max_idx!=-1:
            res.append(words[max_idx])
            max_idx = prev[max_idx]
        res.reverse()
        return res