class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPeak():
            if len(nums) == 1:
                return 0
            if nums[0] < nums[-1]:
                return len(nums) - 1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        peakIdx = findPeak()
        print(peakIdx)
        l, r = 0, len(nums) - 1
        if nums[l] <= target <= nums[peakIdx]:
            r = peakIdx
        else:
            l = peakIdx + 1
        print(f"{l},{r}")
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
