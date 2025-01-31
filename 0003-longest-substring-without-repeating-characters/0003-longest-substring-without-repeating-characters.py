class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        res, ptr = 0, 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[ptr])
                ptr+=1

            visited.add(s[i])
            res = max(res, len(visited))
        return res
