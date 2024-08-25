class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def work(speed):
            cost_hour = 0
            for i in range(0, len(dist) - 1):
                cost_hour += ceil(dist[i] / speed)
            cost_hour += dist[-1] / speed
            return cost_hour <= hour
        check = work(10_000_000)
        if check == False:
            return -1
        l,r = 1, 10_000_000
        while l < r:
            mid = (l + r) // 2
            if work(mid) == False:
                l = mid + 1
            else:
                r = mid
        return l
