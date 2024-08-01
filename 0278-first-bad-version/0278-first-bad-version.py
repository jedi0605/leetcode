# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = -1 , n+1
        while l+1 != r:
            mid = (l+r) //2
            res = isBadVersion(mid)
            if not res:
                l = mid
            else:
                r= mid
        return r