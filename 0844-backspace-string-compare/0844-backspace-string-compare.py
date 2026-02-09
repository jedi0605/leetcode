class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.replaceBackSpace(s) == self.replaceBackSpace(t)
    def replaceBackSpace(self, s: str)->str:
        arr = []
        for c in s:
            if c == "#":
                if len(arr) > 0:
                    arr.pop()
            else:
                arr.append(c)
        print(arr)            
        return "".join(arr)