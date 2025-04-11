class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        tmp = [''] * n

        def dfs(idx):
            if idx == len(tmp):
                res.append("".join(tmp))
                return
            for d in phone_map[digits[idx]]:
                tmp[idx] = d
                dfs(idx+1)
        dfs(0)
        return res 