class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
                continue
            else:
                first = stack.pop()
                sec = stack.pop()
                operate_res = 0
                if t == "+":
                    operate_res = sec + first
                elif t == "-":
                    operate_res = sec - first
                elif t == "*":
                    operate_res = sec * first
                else:
                    operate_res = int(sec / first)
                stack.append(operate_res)
        return stack.pop()
