class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ele = max(nums)
        window = defaultdict(int)  # element, count
        l = 0
        res = 0
        for r in range(len(nums)):
            window[nums[r]] += 1
            while window[max_ele] == k:
                res += len(nums) - r
                window[nums[l]] -= 1
                l += 1
        return res
