class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt= Counter(nums)
        for i in range(len(nums)):
            if cnt[0] != 0:
                nums[i] = 0
                cnt[0]-= 1
            elif cnt[1]!=0:
                nums[i] = 1
                cnt[1]-= 1
            else:
                nums[i] = 2
                cnt[2]-= 1