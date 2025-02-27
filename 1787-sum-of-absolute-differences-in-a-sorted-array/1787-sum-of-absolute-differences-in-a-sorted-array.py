class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        total = sum(nums)
        left_total = 0
        for i in range(len(nums)):
            right_total = total - nums[i] - left_total
            left_size, right_size = i, len(nums) - 1 - i

            tmp = (nums[i] * i - left_total) + (right_total - nums[i] * right_size)
            res.append(tmp)

            left_total+= nums[i]
        return res
