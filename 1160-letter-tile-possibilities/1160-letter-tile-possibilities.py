class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)

        def backtracking():
            res = 0
            for c in cnt:
                if cnt[c] > 0:
                    cnt[c] -= 1
                    res += 1
                    res += backtracking()
                    cnt[c] += 1
            return res

        return backtracking()
