class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {}
        mapping["]"] = "["
        mapping[")"] = "("
        mapping["}"] = "{"
        tracking = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                tracking.append(c)
            else:
                if len(tracking) < 1:
                    return False
                elif tracking[-1] != mapping[c]:
                    return False
                else:
                    tracking.pop()
        return len(tracking) == 0
