class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:                
                l -= 1
                r += 1
            curStr = s[l+1 : r]
            if len(curStr) > len(res):
                res = curStr

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:                
                l -= 1
                r += 1   
            curStr = s[l+1 : r]         
            if len(curStr) > len(res):
                res = curStr
        return res
