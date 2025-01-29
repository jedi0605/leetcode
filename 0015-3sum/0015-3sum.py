class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        first_vi = set()
        res = []

        for i in range(0, len(nums) - 2):
            tmp = nums[i]
            if tmp in first_vi:
                continue
            first_vi.add(tmp)
            l, r = i + 1, len(nums) - 1
            while l != r:
                threeSum = nums[l] + nums[r] + tmp
                if threeSum == 0:
                    res.append([tmp, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
