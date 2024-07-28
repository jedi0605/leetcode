class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def countN(nums: List[int]) -> int:
            l, r = -1, len(nums)

            while l + 1 < r:
                mid = (l + r) // 2
                if nums[mid] >= 0:
                    l = mid
                else:
                    r = mid
            print(l)
            if l == -1:
                return len(nums)
            else:
                return len(nums) - 1 - l

        res = 0
        for row in grid:
            res += countN(row)
        return res
