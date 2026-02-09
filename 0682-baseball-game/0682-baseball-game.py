class Solution:
    def calPoints(self, operations: List[str]) -> int:        
        arr = []

        for s in operations:
            if s == "C" :
                arr.pop()
            elif s == "+":
                tmp = arr[-1] + arr[-2]
                arr.append(tmp)
            elif s =="D":
                arr.append(arr[-1] * 2)                
            else:
                arr.append(int(s))
        return sum(arr)