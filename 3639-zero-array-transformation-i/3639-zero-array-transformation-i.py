class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * len(nums)

        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(nums):
                diff[r + 1] -= 1
        print(diff)
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += diff[i]
            if nums[i] > curr_sum:
                return False
        return True
