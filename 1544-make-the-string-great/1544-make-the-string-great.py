class Solution:
    def makeGood(self, s: str) -> str:
        arr = ['']
        idx = 0
        for c in s:
            lastC = arr[-1]
            # print(lastC)
            if lastC.upper() == c.upper() and lastC.isupper() and c.islower():
                arr.pop()
            elif lastC.upper() == c.upper() and lastC.islower() and c.isupper():
                arr.pop()
            else:
                arr.append(c)
            # print(arr)
        de = ""
        res = de.join(arr)
        return res       
