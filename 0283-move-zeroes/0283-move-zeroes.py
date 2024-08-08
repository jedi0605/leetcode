class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = float("inf")

        for i in range(len(nums)):
            if nums[i] == 0:
                last_zero = min(last_zero, i)
            elif nums[i] != 0 and last_zero != float("inf"):
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
                last_zero += 1
