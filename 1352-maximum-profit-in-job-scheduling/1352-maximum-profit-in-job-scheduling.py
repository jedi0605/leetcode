class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # jobs = zip(startTime,endTime,profit)
        jobs = []
        heap = []
        for i in range(len(startTime)):
            jobs.append( [startTime[i],endTime[i],profit[i]] )
        jobs.sort()
        print(jobs)
        cur_p = 0
        max_p = 0
        for job in jobs:
            s,e,p = job[0],job[1],job[2]
            while heap and s >= heap[0][0]:
                end, cur_p = heapq.heappop(heap)
                max_p = max(max_p,cur_p)
            heapq.heappush(heap, [e, p + cur_p])
        print(heap)
        for e,p in heap:
            max_p = max(max_p,p)
        return max_p
