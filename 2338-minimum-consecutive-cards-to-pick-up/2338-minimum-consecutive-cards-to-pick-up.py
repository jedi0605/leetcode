class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')        
        maps = defaultdict(int) # nums / idx

        for idx, num in enumerate(cards):
            if num in maps:
                res = min(res,idx - maps[num] +1 )
                maps[num] = idx
            else:
                maps[num] = idx
        return res if res!=float('inf') else -1