class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_p = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                subS = s[l : r + 1]
                if subS == subS[::-1] and len(subS) >= len(max_p):
                    max_p = subS
                l -= 1
                r += 1
                
            l,r = i,i+1
            while l >= 0 and r < len(s):
                subS = s[l : r + 1]
                if subS == subS[::-1] and len(subS) >= len(max_p):
                    max_p = subS
                l -= 1
                r += 1
               
        return max_p
