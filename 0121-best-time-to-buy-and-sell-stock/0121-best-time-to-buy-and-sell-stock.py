class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowP = float("inf")
        res = 0
        for p in prices:
            if lowP > p:
                lowP = p
            res = max(p-lowP, res)
        return res