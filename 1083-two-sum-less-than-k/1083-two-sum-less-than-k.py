class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0, len(nums)-1
        print(nums)
        res = -1
        while l<r:
            sum = nums[l]+nums[r]
            if sum >= k:
                r-=1
            else:
                l+=1
                res = max(res,sum)
        return res
