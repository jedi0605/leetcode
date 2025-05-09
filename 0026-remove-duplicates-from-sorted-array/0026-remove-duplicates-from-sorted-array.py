class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [0,0,1,1,1,2,2,3,3,4]
        #         l
        #             r
        # pointer left side
        l = 0
        for r in range(1,len(nums)):
            if nums[r] > nums[l]: # swap
                nums[l+1],nums[r] = nums[r],nums[l+1]
                l = l+1
        return l + 1

