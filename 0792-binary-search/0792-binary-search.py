class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums)

        while l+1<r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return l if nums[l] == target else -1