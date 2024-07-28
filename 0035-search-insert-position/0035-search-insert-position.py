class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)

        while l + 1 != r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r
