class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatArr = []
        for a in grid:
            for i in a:
                flatArr.append(i)
        flatArr.sort()
        preMod = flatArr[0] % x
        for i in flatArr:
            if i % x != preMod:
                return -1
        total = sum(flatArr)
        pre = 0 
        res = float("inf")
        
        for i in range(len(flatArr)):
            cost_left = i * flatArr[i] - pre
            cost_right = total - pre - ((len(flatArr)-i) * flatArr[i])
            operations = (cost_left+cost_right) //x
            pre += flatArr[i]
            res = min(operations,res)
        return res
