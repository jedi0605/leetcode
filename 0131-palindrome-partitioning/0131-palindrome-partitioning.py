class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        tmp = []

        def dfs(i):
            if i >= len(s):
                res.append(tmp[:])
                return
            for j in range(i,len(s)):
                subStr = s[i:j+1]
                if subStr == subStr[::-1]:
                    tmp.append(subStr)
                    dfs(j+1)
                    tmp.pop()
        dfs(0)
        return res