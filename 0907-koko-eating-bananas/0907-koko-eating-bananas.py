class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def work(eat):
            total = 0
            for p in piles:
                times = 0
                times = p // eat
                if p % eat != 0:
                    times += 1
                total += times
            return total <= h

        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if work(mid):
                r = mid
            else:
                l = mid + 1
        return l
