class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        res = []
        for i in range( len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    cur_arr = [nums[i]] + dp[j]
                    if len(cur_arr) > len(dp[i]):
                        dp[i] = cur_arr
            print(dp[i])
            if len(dp[i])>len(res):
                res = dp[i]
        return res
