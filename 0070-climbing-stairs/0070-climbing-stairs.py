class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        base_one = 1
        base_two = 2
        res = 0
        for i in range(2, n):
            res = base_one + base_two
            base_one = base_two
            base_two = res
        return res
