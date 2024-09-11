class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coin = ((mid + 1) * mid) // 2
            print(coin)
            if coin <= n:
                l = mid + 1
            else:
                r = mid -1
        return r
