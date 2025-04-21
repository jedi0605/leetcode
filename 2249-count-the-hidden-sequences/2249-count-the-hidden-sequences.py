class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        def worked(mid):
            start = mid
            for diff in differences:
                tmp = start + diff
                if tmp < lower:
                    return -1  # too small
                if tmp > upper:
                    return 1  # too big
                start = tmp
            return 0

        left, right = lower, upper
        while left <= right:
            mid = (left + right) // 2
            res = worked(mid)
            if res == -1:
                left = mid + 1
            else:
                right = mid - 1

        lowest = left
        if lowest > upper:
            return 0
        left, right = lower, upper
        while left <= right:
            mid = (left + right) // 2
            res = worked(mid)
            if res == 1:
                right = mid - 1
            else:
                left = mid + 1

        highest = right
        return highest - lowest + 1
