class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = (1 << 32) + num
        hexStr = "0123456789abcdef"
        res = ""
        while num > 0:
            h_s = hexStr[ num %16]
            res = h_s + res
            num = num // 16
        return res

