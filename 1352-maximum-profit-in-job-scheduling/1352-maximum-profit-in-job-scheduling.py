class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs =sorted( zip(startTime,endTime,profit))
        heap = []
        maxProfit = 0
        for s,e,p in jobs:
            
            while heap and heap[0][0]<=s:
                start, profit = heappop(heap)                
                maxProfit = max(profit,maxProfit)
            heappush(heap, (e,p+maxProfit) )
        for e,p in heap:
            maxProfit = max(p,maxProfit)
        return maxProfit