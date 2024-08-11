class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        print(envelopes)
        dp = []

        for env in envelopes:
            idx = bisect_left(dp, env[1])
            if idx == len(dp):
                dp.append(env[1])
            else:
                dp[idx] = env[1]
        return len(dp)
