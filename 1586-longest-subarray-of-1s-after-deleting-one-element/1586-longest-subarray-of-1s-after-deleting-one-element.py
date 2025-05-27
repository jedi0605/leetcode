class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zero_cnt = 0, 0
        res = 0
        for idx, val in enumerate(nums):
            zero_cnt += 1 if val == 0 else 0

            while zero_cnt > 1:
                zero_cnt -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res, idx - l)
        return res
