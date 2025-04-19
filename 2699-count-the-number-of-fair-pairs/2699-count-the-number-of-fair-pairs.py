class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # brute force
        nums.sort()
        res = 0

        for i in range(len(nums) - 1):
            # 0, 1, 4, 4, 5, 7
            lo = lower - nums[i]
            hi = upper - nums[i]
            left_b = bisect_left(nums, lo,i+1)
            right_b = bisect_right(nums, hi,i+1)
            res += right_b - left_b

        return res
