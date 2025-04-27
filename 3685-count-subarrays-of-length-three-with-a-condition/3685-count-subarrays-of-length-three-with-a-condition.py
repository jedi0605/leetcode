class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(2,len(nums)):
            first,sec,thd = nums[i-2], nums[i-1], nums[i]
            if (first+thd) * 2 == sec:
                res +=1
        return res
