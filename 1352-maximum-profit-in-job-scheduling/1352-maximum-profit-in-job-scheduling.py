class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        endArr = [e for s,e,p in jobs]
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2] # default profit
        
        for i in range(1,len(jobs)):
            s = jobs[i][0]
            e = jobs[i][1]
            p = jobs[i][2]
            # print(f"{s}.{e}.{p}")
            idx = bisect_right(endArr, s) -1 # find the last s in endArr
            # print(idx)
            dp[i] = max(dp[i-1], (dp[idx] if idx>=0 else 0) +p)
            # print(dp)
        return dp[-1]
        # jobs =sorted( zip(startTime,endTime,profit))
        # heap = []
        # maxProfit = 0
        # for s,e,p in jobs:

        #     while heap and heap[0][0]<=s:
        #         start, profit = heappop(heap)
        #         maxProfit = max(profit,maxProfit)
        #     heappush(heap, (e,p+maxProfit) )
        # for e,p in heap:
        #     maxProfit = max(p,maxProfit)
        # return maxProfit
