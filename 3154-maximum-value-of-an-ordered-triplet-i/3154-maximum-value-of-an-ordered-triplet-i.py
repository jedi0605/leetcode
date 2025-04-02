class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        leftMax = [0] * len(nums)
        for i in range(1,len(nums)):
            leftMax[i] = max(leftMax[i-1],nums[i-1])        
        rightMax = [0] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],nums[i+1])
        res = 0
        for i in range(1,len(nums)-1):
            res = max(res, (leftMax[i]- nums[i])*rightMax[i] )
        return res