class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        first_vi = set()
        print(nums)
        for i in range(0, len(nums) - 2):
            if nums[i] in first_vi:
                continue
            first_vi.add(nums[i])
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l <r :
                        l += 1
        return res
