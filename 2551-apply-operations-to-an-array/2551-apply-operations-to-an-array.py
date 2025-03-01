class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # do operation

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        print(nums)
        # swap 0
        cur = 0
        lastZ = -1
        while cur < len(nums):
            if nums[cur] == 0 and lastZ == -1:
                lastZ = cur
                cur += 1
            elif nums[cur] != 0 and lastZ != -1:
                nums[cur], nums[lastZ] = nums[lastZ], nums[cur]
                cur = lastZ
                lastZ = -1
            else:
                cur += 1
        print(nums)
        return nums
