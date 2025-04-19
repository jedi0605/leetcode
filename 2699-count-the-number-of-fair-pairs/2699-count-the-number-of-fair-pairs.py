class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1):
            minReq = lower - nums[i]
            maxReq = upper - nums[i]
            low = bisect_left(nums, minReq, i+1)
            high = bisect_right(nums, maxReq, i+1)
            ans += high - low
        return ans