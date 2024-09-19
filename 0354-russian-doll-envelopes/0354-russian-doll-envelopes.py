class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x : (x[0], -x[1]))
        print(envelopes)
        dp = []
        dp.append(envelopes[0][1])
        for x,y in envelopes:
            idx = bisect_left(dp, y)
            if idx >= len(dp):
                dp.append(y)
            else:
                dp[idx] = y
        return len(dp)