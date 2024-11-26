class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a) - 1
        blen = len(b) - 1
        res = deque()
        carry = 0
        while alen >= 0 or blen >= 0:
            tmp = carry
            if alen >= 0 and a[alen] != "0":
                tmp += 1
            if blen >= 0 and b[blen] != "0":
                tmp += 1

            if tmp == 3:
                carry = 1
                res.appendleft("1")
            elif tmp == 2:
                carry = 1
                res.appendleft("0")
            elif tmp == 1:
                carry = 0
                res.appendleft("1")
            else:
                carry = 0
                res.appendleft("0")
            alen -= 1
            blen -= 1
        if carry == 1:
            res.appendleft("1")
        return ''.join(res)