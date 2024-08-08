class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # res = []
        # potions.sort()
        # for i in range(len(spells)):            
        #     s = spells[i]
        #     l,r = -1,len(potions)
        #     print(ceil(success/s))
        #     while l+1!=r:
        #         mid = (l+r) //2
        #         if potions[mid] * s < success:
        #             l = mid
        #         else:
        #             r = mid
        #     print(r)
        #     res.append(len(potions) - r)
        # return res
        res = []
        potions.sort()
        last = potions[-1]
        for i in range(len(spells)):            
            s = spells[i]            
            check = ceil(success/s)
            if check > last:
                res.append(0)
                continue
            idx = bisect_left(potions, check)
            res.append(len(potions) - idx)
        return res