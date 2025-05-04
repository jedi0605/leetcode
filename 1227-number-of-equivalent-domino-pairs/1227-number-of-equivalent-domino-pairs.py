class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt_map = defaultdict(int)
        for a, b in dominoes:
            print(f"{a},{b}")
            if a > b:
                cnt_map[(b, a)] += 1
            else:
                cnt_map[(a, b)] += 1

        res = 0
        for freq in cnt_map.values():
            res += freq * (freq - 1) // 2
        return res
