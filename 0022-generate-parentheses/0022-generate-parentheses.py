class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []
        def dfs(openN,closeN):
            if closeN == n:
                res.append(''.join(tmp))
                return
            if openN<n:
                tmp.append('(')
                dfs(openN+1, closeN)
                tmp.pop()
            if closeN < n and closeN<openN:
                tmp.append(')')
                dfs(openN, closeN+1)
                tmp.pop()
        dfs(0,0)
        return res