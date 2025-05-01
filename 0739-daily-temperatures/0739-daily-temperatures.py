class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]  # nums, idx
        # res = [1,1,0,0,0,1,0,0]
        # i = 5, stack = [(75,2), (71,3), (69,4)]
        # temperatures[i] = 72
        # stack[-1] = 69
        #       val ,idx = 69,4 

        for i in range(1, len(temperatures)):

            while len(stack)>0 and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))
        return res
