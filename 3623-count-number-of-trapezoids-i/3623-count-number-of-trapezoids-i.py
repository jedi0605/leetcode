class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        groupedy = defaultdict(list)
        for x, y in points:
            groupedy[y].append(x)
        

        total = 0
        up = 0

        for key, val in groupedy.items():
            # print(comb(len(val), 2))
            total += up * comb(len(val), 2)
            up += comb(len(val), 2)
        return total % MOD
