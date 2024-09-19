class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =[1] * len(nums)

        for i in range(len(nums)):
            cur_max = 1
            for j in range(0,i):
                if nums[i] > nums[j]:
                    cur_max = max(dp[j]+1,cur_max)
            dp[i] = cur_max

        return max(dp)