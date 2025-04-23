class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sumNum(num:int) ->int:
            num_str = str(num)
            res = 0
            for c in num_str:
                res+=int(c)
            return res
        arr = [0] * (n+1)
        for i in range(1,n+1):
            arr[ sumNum(i)]+=1
        print(arr)
        max_cnt = max(arr)
        res = 0
        for a in arr:
            if a == max_cnt:
                res+=1
        return res