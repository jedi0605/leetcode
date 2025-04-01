class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                curStr = s[l : r + 1]
                if curStr == curStr[::-1]:
                    if len(curStr) > len(res):
                        res = curStr
                    l -= 1
                    r += 1
                else:
                    break
            l, r = i, i+1
            while l >= 0 and r < len(s):
                curStr = s[l : r + 1]
                if curStr == curStr[::-1]:
                    if len(curStr) > len(res):
                        res = curStr
                    l -= 1
                    r += 1
                else:
                    break
        return res
