class Solution:
    def myPow(self, x: float, n: int) -> float:
        def help(power):
            if power == 0:
                return 1
            if power == 1:
                return x
            res = help(power//2)
            if power%2 == 1:
                return res * x * res
            else:
                return res * res
        ans = help(abs(n))
        
        return ans if n >=0 else 1/ans
