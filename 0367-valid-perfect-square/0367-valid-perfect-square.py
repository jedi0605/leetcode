class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0 , num
        while l+1 != r:
            mid = (l+r) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid
            else :
                r = mid
        return False
