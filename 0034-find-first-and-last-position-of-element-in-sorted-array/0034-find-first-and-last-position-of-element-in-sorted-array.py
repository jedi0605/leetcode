class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        print([left, right])
        if left == len(nums) or nums[right]!=target:
            return [-1, -1]
        # if nums[left] != target or nums[right] != target:
            # return [-1, -1]
        return [left, right]

        # def findLeft(target):
        #     l, r = -1, len(nums)
        #     while l + 1 != r:
        #         mid = (l + r) // 2
        #         if nums[mid] < target:
        #             l = mid
        #         else:
        #             r = mid
        #     if r == len(nums):
        #         return -1
        #     return r if nums[r] == target else -1

        # def findRight(target):
        #     l, r = -1, len(nums)
        #     while l + 1 != r:
        #         mid = (l + r) // 2
        #         if nums[mid] <= target:
        #             l = mid
        #         else:
        #             r = mid
        #     print(l)
        #     return l if nums[l] == target else -1

        # left = findLeft(target)
        # if left == -1:
        #     return [-1, -1]
        # right = findRight(target)
        # return [left, right]
