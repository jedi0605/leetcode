class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch2(nums, start, end, target):
            l, r = start - 1, end
            while l + 1 != r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid

            if r == len(nums):
                return -1
            return r if nums[r] == target else -1

        def bSearch(nums):
            l, r = -1, len(nums)

            while l + 1 != r:
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            return r


        small_idx = bSearch(nums)
        start, end = 0, 0

        if nums[small_idx] <= target <= nums[-1]:  # right side
            start, end = small_idx, len(nums)
        else:
            start, end = 0, small_idx

        return bSearch2(nums, start, end, target)
