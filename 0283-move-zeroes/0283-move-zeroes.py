class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = -1 # point to first 0

        for i in range(len(nums)):
            # init first 0
            if nums[i] == 0 and l == -1:
                l = i
            elif nums[i] != 0 and l != -1:
                nums[i],nums[l] = nums[l],nums[i]
                l = l+1
