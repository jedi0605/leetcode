class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def work(cap):
            i = 0
            res = 0
            while i < len(nums):
                if nums[i] <= cap:
                    res += 1
                    i += 2
                else:
                    i += 1
            return res >= k

        l, r = min(nums), max(nums)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if work(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
