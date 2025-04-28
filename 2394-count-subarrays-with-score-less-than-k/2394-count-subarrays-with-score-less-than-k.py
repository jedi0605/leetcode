class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        sub_total = 0

        for r in range(len(nums)):
            sub_total+=nums[r]
            while sub_total * (r-left+1) >=k:
                sub_total-=nums[left]
                left+=1
            res += (r-left+1)
        return res