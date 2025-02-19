class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def dfs(i):
            if i == len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):
                cur_str = s[i : j + 1]
                if cur_str == cur_str[::-1]:
                    sub.append(cur_str)
                    dfs(j + 1)
                    sub.pop()

        dfs(0)
        return res
