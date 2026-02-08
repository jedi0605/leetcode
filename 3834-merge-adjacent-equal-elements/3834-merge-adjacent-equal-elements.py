class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            res.append(n)
            while len(res)>1 and res[-1] == res[-2]:
                res.pop()
                res[-1]*=2
        return res