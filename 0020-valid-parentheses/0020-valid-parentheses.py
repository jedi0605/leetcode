class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {")":"(" , "]":"[", "}":"{"}
        for p in s:
            if p == "(" or p =="[" or p == "{":
                stack.append(p)
            else:
                if len(stack) == 0 :
                    return False
                c = stack.pop()
                if maps[p] != c:
                    return False
        return len(stack) == 0