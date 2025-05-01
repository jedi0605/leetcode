class Solution:
    def calculate(self, s: str) -> int:
        op = 1 # previs sign
        stack = []
        num = 0
        tmp = 0
        for c in s: # char
            if c.isdigit():
                tmp= tmp * 10 + int(c)
            if c == "+" or c == "-":
                num = num + tmp * op
                tmp = 0                
                op = 1 if c == "+" else -1                            
            if c == "(":
                stack.append(num)
                stack.append(op)
                num = 0
                op = 1
                tmp = 0
            if c == ")":
                num += tmp * op
                num *= stack.pop()
                num+= stack.pop()
                tmp = 0        
        return num + (tmp * op)
