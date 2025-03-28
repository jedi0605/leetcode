class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for c in row:
                arr.append(c)
        arr.sort()
        checkMod = arr[0] % x
        for i in arr:
            if i % x != checkMod:
                return -1
        pre_sum = 0
        res = float("inf")
        total = sum(arr)
        for i in range(len(arr)):
            pre_sum += arr[i]
            left_op = ((arr[i]*(i+1)) - pre_sum) // x
            

            right_total = total - pre_sum
            right_len = len(arr) - i - 1
            right_op = (right_total - (right_len * arr[i])) // x
            res = min(left_op + right_op, res)
        return res
