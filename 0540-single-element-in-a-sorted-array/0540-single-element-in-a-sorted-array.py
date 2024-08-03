class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Brute force
        # for i in range(0, len(nums) - 2, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return -1
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l + r) // 2
            are_even = (r - mid) % 2

            if nums[mid] == nums[mid + 1]:
                if are_even == 0:
                    l = mid + 2
                else:
                    r = mid -1

            elif nums[mid] == nums[mid - 1]:
                if are_even == 0:
                    r = mid -2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]
