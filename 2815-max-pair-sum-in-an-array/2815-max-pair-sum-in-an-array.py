class Solution:
    def maxSum(self, nums: List[int]) -> int:
        large = []
        dis = {} # max_digit, max_val
        res = -1
        for n in nums:
            max_digit = max(int(d) for d in str(n))
            if max_digit in dis:
               res = max(res, dis[max_digit] + n)
               dis[max_digit] = max(dis[max_digit],n)
            else:
                dis[max_digit] = n

        return res
