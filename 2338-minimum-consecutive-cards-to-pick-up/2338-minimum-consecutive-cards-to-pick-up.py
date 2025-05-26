class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')

        
        have_pair = False
        maps = defaultdict(int) # nums / cnt

        l = 0
        # 3:1
        for r in range(len(cards)):
            num =cards[r] 
            maps[num]+=1
            if maps[num] >1:
                have_pair = True
                # res = min(res, r-l+1)
            while have_pair:
                res = min(res, r-l+1)
                maps[cards[l]]-=1
                if cards[l] == num:
                    have_pair = False
                l+=1
        return res if res != float('inf') else -1