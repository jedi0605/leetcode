class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        res = []
        potions.sort()
        for i in range(len(spells)):            
            s = spells[i]
            l,r = -1,len(potions)
            while l+1!=r:
                mid = (l+r) //2
                if potions[mid] * s < success:
                    l = mid
                else:
                    r = mid
            print(r)
            res.append(len(potions) - r)
        return res
