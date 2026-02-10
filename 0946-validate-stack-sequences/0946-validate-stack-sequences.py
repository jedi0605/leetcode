class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []
        popIdx = 0
        for p in pushed:
            arr.append(p)
            
            while popIdx < len(popped) and arr and arr[-1] == popped[popIdx]:     
                print(arr)           
                arr.pop()
                popIdx+=1
        return len(arr) == 0
            