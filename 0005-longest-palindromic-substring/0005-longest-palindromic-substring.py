class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_p = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                subStr = s[i:j+1]
                if subStr == subStr[::-1] and len(subStr)> len(max_p):
                    max_p = subStr
        return max_p
