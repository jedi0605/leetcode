class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(p):
            if p == 0:
                return 1
            if p == 1:
                return x
            a = helper(p // 2)
            if p % 2 == 1:
                return a * a * x
            else:
                return a * a 

        res = helper( abs( n))
        return res if n > 0 else 1 / res
