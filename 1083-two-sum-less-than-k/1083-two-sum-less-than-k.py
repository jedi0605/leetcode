class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        # if nums[0] + nums[-1] > k:
        #     return -1
        print(nums)
        l, r = 0 , len(nums)-1
        res = -1
        while l<r:
            if nums[r] > k:
                r -=1
            elif nums[r] + nums[l] < k:
                res = max(res, nums[r] + nums[l])
                l+=1
            else:
                r-=1
                l =0
        return res