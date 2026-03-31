class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # dist = {}
        res = -inf
        total = sum(nums)
        cnt = Counter(nums)

        for i in range(len(nums)):
            cnt[nums[i]] -= 1
            outlier = total - 2 * nums[i]
            if cnt[outlier] > 0:
                res = max(res, outlier)
            cnt[nums[i]] += 1
        return res
