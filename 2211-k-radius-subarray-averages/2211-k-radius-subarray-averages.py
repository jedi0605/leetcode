class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums) or (k *2+1) > len(nums):
            return [-1] * len(nums)

        res = [-1] * len(nums)
        window_size = (k * 2 + 1)
        init_arr = nums[:window_size]
        init_sum = sum(init_arr)
        res[k] = init_sum // (k *2+1)

        print(init_arr)
        for i in range(window_size,len(nums)):
            init_sum = init_sum - nums[i - window_size] + nums[i]
            res[i-k] = init_sum // (k *2+1)            
        return res