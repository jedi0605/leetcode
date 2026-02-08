class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = [] # str arr
        targetIdx = 0
        for i in range(1,target[-1]+1):
            ops.append("Push")
            if i != target[targetIdx]:
                ops.append("Pop")
            else:
                targetIdx+=1
        return ops


