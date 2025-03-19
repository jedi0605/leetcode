class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        r = 0
        while r < len(nums):
            if nums[r] != 1 and r + 2 < len(nums):
                # flipping
                nums[r] = 1
                nums[r + 1] = 0 if nums[r + 1] == 1 else 1
                nums[r + 2] = 0 if nums[r + 2] == 1 else 1
                res += 1
            r += 1

        return res if nums[-1] == 1 and nums[-2] == 1 else -1
