class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s :
            return 0
        first = 0
        leading = 1
        if s[0] == "+":
            first = 1
        elif s[0] == "-":
            leading = -1
            first = 1
        
        res = 0
        for i in range(first, len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
        res = res * leading
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -(2**31):
            return -(2**31)
        return res
