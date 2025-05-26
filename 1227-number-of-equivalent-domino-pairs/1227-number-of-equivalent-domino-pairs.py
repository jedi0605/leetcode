class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        maps= defaultdict(int) # pairs

        for a,b in dominoes:
            if (a,b) in maps:
                res +=maps[(a,b)]
                maps[(a,b)] += 1
            elif (b,a) in maps:
                res+=maps[(b,a)]
                maps[(b,a)] += 1
            else:
                maps[(a,b)] = 1
        return res