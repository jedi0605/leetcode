class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        print(s[::-1])

        def dfs(i):
            if i >= len(s):
                res.append(sub[:])
                return

            for j in range(i, len(s)):
                subS = s[i : j + 1]
                if subS == subS[::-1]:
                    sub.append(subS)
                    dfs(j + 1)
                    sub.pop()

        dfs(0)
        return res
