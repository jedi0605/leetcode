class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for c in s:
            arr.append(c)
            while arr and arr[-1] == "*":
                arr.pop()
                arr.pop()
        return "".join(arr)