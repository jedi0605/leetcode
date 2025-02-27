class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        for i in range(len(nums) - 1):
            left_sum[i + 1] = left_sum[i] + nums[i]

        for i in range(len(nums) - 1,0,-1):
            right_sum[i-1] = right_sum[i] + nums[i]
        print(left_sum)
        print(right_sum)
        for i in range(len(nums)):
            r = len(nums) - 1 - i
            tmp = (nums[i] * i - left_sum[i] ) + (right_sum[i] - nums[i] * r)
            res.append(tmp)
        return res
        #  (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) +
        #             ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1))
        #  i = 2
        # 5 * 2 - (2 + 3) + (0 - 5 * (3-2-1))
        # 10 - 5 = 5
        # ()
        #   i = 1
        # .  (3 * 1 - 2) + (5) - 3 * (3-1-1)
        #    1 +  2 = 3
        #   i = 0
        # .  ( 2 * 0 - (0) ) +  ((3+5) - 2*(3-0-1))
        # .   -2 +                8 - 4
        #    2
        # [2,3,5]
        # . ^ 2-2, 2-3,2-5
        # .   3-2, 3-3,3-5
        # .     ^
        # 1,4,6,8,10
        # 1-1,1-4,1-6,1-8,1-10
        #
        # res = []
        # for n in nums:
        #     cur_sum = 0
        #     for m in nums:
        #         cur_sum += abs(n-m)
        #     res.append(cur_sum)
        # return res
