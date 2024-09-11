class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        l,r = 0, x // 2

        while l<=r:
            mid = (l+r) // 2
            num = mid * mid
            if num == x:
                return mid
            if num < x:
                l = mid + 1
            else:
                r = mid - 1

        return r
