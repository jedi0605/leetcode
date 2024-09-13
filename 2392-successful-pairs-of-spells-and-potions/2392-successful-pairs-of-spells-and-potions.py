class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0] * len(spells)
        potions.sort()
        for s in range(len(spells)):
            cnt = 0
            target_val = math.ceil( success/spells[s])
            idx =  bisect_left(potions,target_val)
            res[s]=len( potions) - idx

            # print(f"{target_val}, {idx}")
            # for p in range(len(potions)):
            #     val = spells[s] * potions[p]
            #     if val >= success:
            #         break
        return res