class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, sum(candies)

        def work(mid):
            if mid == 0:
                return False
            res = 0  # if candies[i] can seperate by mid then res+1
            for c in candies:
                res += c // mid
            return res >= k

        while l <= r:
            mid = (l + r) // 2
            if work(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r if r>=0 else 0
