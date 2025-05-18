class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pre_s = []

        for c in s:
            if 'a'<=c<='z' or '0'<=c<='9':
                pre_s.append(c)
        pre_s = "".join(pre_s)
        return pre_s == pre_s[::-1]