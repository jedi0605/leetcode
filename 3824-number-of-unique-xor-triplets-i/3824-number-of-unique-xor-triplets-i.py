class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        return 2 ** len(nums).bit_length()