class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        max_pre = 0
        min_pre = 0

        for n in nums:
            max_pre = max(max_pre+n,n)
            min_pre = min(min_pre+n,n)
            res = max(max_pre,res)
            res = max(abs(min_pre),res)
        return res