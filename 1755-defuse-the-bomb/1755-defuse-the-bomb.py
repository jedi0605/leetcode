class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0:
            return res
        
        if k >0:
            
            init_sum =sum( code[:k+1]) - code[0]
            print(init_sum)
            res[0] = init_sum
            for i in range(1,len(code)):
                init_sum -= code[i]
                next_idx = (i + k) %len(code)
                init_sum +=code[next_idx]
                res[i] = init_sum
        if k<0:
            k = k * -1
            code = code[::-1]
            print(code)
            init_sum =sum( code[:k+1]) - code[0]
            print(init_sum)
            res[len(code)-1] = init_sum
            for i in range(1,len(code)):
                init_sum -= code[i]
                next_idx = (i + k) %len(code)
                init_sum +=code[next_idx]
                res[len(code)-1 - i] = init_sum

        return res
        # if k<0: