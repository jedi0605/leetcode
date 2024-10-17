# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = -1,n

        while left+1!=right:
            mid = (left+right) // 2
            if isBadVersion(mid) == False:
                left = mid
            else:
                right = mid
        return right