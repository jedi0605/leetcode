class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = bisect_left(nums, target)
        if s == len(nums) or nums[s] != target:
            return -1
        return s