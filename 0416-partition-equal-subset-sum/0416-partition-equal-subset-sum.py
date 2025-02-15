class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextDp = set()
            for d in dp:
                nextDp.add(d + nums[i])
                nextDp.add(d)
            dp = nextDp

        return target in dp
