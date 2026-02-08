class Solution:
    def resultingString(self, s: str) -> str:
        arr = []
        for c in s:
            arr.append(c)
            # print(arr)
            while len(arr) > 1 and self.consecutiveCht(arr[-1],arr[-2]):
                arr.pop()
                arr.pop()
        # print(f"res {arr}")
        dec = ""
        return dec.join(arr)

    def consecutiveCht(self,a,b) -> bool:
        a_next =''
        a_pre = ''
        
        if a == 'z':
            a_next = 'a'
        else:
            a_next = chr(ord(a) + 1)

        if a == 'a':
            a_pre = 'z'
        else:
            a_pre = chr(ord(a) - 1)
        if a_next == b:
            return True
        elif a_pre == b:
            return True
        else:
            return False