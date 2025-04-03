class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i-1])

        right_max = [0] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i+1])
        res = 0
        print(left_max)
        print(right_max)
        for i in range(1, n - 1):
            res = max(res, (left_max[i] - nums[i]) * right_max[i])
        return res
