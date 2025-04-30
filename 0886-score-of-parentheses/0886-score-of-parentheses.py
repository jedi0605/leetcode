class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0

        stack = []

        for c in s:
            if c == "(":
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(1, 2 * res)
        return res
