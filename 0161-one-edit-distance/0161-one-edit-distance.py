class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # check len
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        # Type 1. replace 2. delete 3. append
        replace, delete, append = False, False, False
        if len(s) == len(t):
            replace = True
        elif len(s) > len(t):
            delete = True
        else:
            append = True

        s1, s2 = 0, 0
        edit = False
        while s1 < len(s) and s2 < len(t):
            if s[s1] == t[s2]:
                s1 += 1
                s2 += 1
            else:
                if edit == True:
                    return False
                edit = True
                if replace:
                    s1 += 1
                    s2 += 1
                elif delete:
                    s1 += 1
                else:
                    s2 += 1
        return True

        # m = len(s)
        # n = len(t)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m + 1):
        #     for j in range(n + 1):
        #         if i == 0:
        #             dp[i][j] = j
        #         elif j == 0:
        #             dp[i][j] = i
        #         elif s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        # return True if dp[-1][-1] == 1 else False
