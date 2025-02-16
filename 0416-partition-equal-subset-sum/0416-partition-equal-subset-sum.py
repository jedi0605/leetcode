class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0: return False
        target = total//2
        dp = set()
        dp.add(0)

        for n in nums:
            newDp = set()
            for d in dp:
                newDp.add(d+n)
                newDp.add(d)
            dp = newDp
        return target in dp