class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 ==1:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        for n in nums:
            copy_dp = dp.copy()
            for d in copy_dp:
                dp.add(n + d)
        return target in dp
