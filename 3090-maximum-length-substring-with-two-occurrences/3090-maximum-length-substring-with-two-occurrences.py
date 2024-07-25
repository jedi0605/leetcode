class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        res = 0
        maps = defaultdict(int)
        for r in range(len(s)):
            c = s[r]
            while maps[c] >= 2:
                res = max(sum(maps.values()), res)
                maps[s[l]] -= 1
                l += 1
            maps[c] += 1
        return max(sum(maps.values()), res)
