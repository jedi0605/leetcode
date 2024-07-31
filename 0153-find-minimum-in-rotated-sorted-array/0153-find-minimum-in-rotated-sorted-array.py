class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = -1 ,len(nums)

        while l+1 != r:
            mid = (l+r) //2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]