class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr = 0
        visited = set()
        res = 0
        for i in range(len(s)):
            print(visited)
            if s[i] not in visited:
                visited.add(s[i])
                res = max(res, len(visited))
            else:
                while s[i] in visited:
                    cht = s[ptr]
                    visited.remove(cht)
                    ptr += 1
                visited.add(s[i])
        return res
