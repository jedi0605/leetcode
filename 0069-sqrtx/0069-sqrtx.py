class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l, r = -1,x
        ans = 0
        while l+1!=r:
            mid = (l+r) // 2
            ans = mid
            res = mid * mid
            if res < x:                
                l = mid
            else:
                r= mid

        return ans
