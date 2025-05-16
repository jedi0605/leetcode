class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming1(a, b):
            if len(a) != len(b):
                return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_idx = 0
        for i in range(n):
            for j in range(i):
                if groups[i]!=groups[j] and hamming1(words[i], words[j]):
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        prev[i] = j
            if dp[i] > max_len:
                max_len=dp[i]
                max_idx = i
        res = []
        cur = max_idx
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]
        res.reverse()
        return res