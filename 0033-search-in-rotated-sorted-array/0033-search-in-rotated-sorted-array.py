class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def searhPeak():
            if len(nums) == 1:
                return 0
            if nums[0] < nums[-1]:
                return len(nums) - 1  # no rotation
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        peak = searhPeak()
        print(peak)
        l, r = 0, len(nums) - 1
        if nums[l] <= target <= nums[peak]:
            r = peak
        else:
            l = peak + 1

        print(f"{l},{r}")
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return -1