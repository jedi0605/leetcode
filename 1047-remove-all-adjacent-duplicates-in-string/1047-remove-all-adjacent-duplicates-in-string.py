class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = ['']
        res = ""
        for c in s:
            lastC = arr[-1]
            if c == lastC:
                arr.pop()
            else:
                arr.append(c)
        joinStr = res.join(arr)
        return joinStr