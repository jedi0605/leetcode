class Solution:
    def arrangeCoins(self, n: int) -> int:
        # brute force
        # r = 1
        # while (n-r) >= 0:
        #     n -= r
        #     r+=1
        # return r - 1

        l, r = 1, n
        res = 0
        while l <= r:
            k = (l + r) // 2
            space = (k / 2) * (k + 1)
            if space > n:
                r = k - 1
            else:                
                res = max(res, k)
                l = k + 1
        return res
