class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for c in s:
            if len(arr) <2:
                arr.append(c)
            elif c != 'c':
                arr.append(c)
            else:
                if arr[-1]=='b' and arr[-2]=='a':

                    arr.pop()
                    arr.pop()               
                    
                else:         
                    return False
        return True if len(arr) == 0 else False
        