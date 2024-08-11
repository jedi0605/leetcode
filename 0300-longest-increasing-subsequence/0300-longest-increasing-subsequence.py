class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            idx = bisect_left(dp, n)
            if idx == len(dp):
                dp.append(n)
            else:
                dp[idx] = n
        return len(dp)

        # T:O(n^2) S:(n)
        # dp = [1] * len(nums)
        # for i in range(1,len(nums)):
        #     for j in range(0,i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        # return max(dp)