class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = -1 ,100_000
        while l+1 !=r:
            mid = (l+r) // 2
            res = mid * mid
            if res == num:
                return True
            if res < num:
                l = mid
            else:
                r = mid
        return False