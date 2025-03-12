class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        print(f"{l},{r}")
        lcount = l
        rcount = len(nums) - r
        return max(lcount,rcount)
