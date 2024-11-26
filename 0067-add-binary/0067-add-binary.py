class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        s = ""
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i-=1
            if j >= 0:
                carry += int(b[j])
                j-=1
            s = str(carry %2) +s
            carry = carry // 2
            
        if carry == 1:
            s = "1"+s
        return s
