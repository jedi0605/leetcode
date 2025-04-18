class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(s: str) -> str:
            if s == "":
                return ""
            res = ""
            l = 0
            for r in range(len(s)):
                if s[l] == s[r]:
                    continue
                else:
                    res += str(r - l) + s[l]
                    l = r
            res += str(len(s) - l) + s[l]
            return res
        look_up = [""] * (n+1)
        for i in range(1,n+1):
            if i == 1:
                look_up[i] = "1"
            else:
                look_up[i] = RLE(look_up[i-1])
        print(look_up)
        return look_up[n]
