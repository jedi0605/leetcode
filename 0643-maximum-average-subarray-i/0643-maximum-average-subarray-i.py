class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        res = max(res,cur_sum)
        for i in range(k, len(nums)):
            cur_sum -= nums[i - k]
            cur_sum += nums[i]
            res = max(res, cur_sum)

        return res / k
