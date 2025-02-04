class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        tmp = 1
        for i in range(1, len(nums)):
            tmp = tmp * nums[i - 1]
            res[i] = res[i] * tmp
        return res

        # l_r = [1] * len(nums)
        # r_l = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     l_r[i] = l_r[i - 1] * nums[i - 1]
        # for i in range(len(nums) - 2, -1, -1):
        #     r_l[i] = r_l[i + 1] * nums[i + 1]
        # for i in range(len(nums)):
        #     l_r[i] = l_r[i] * r_l[i]
        # return l_r
