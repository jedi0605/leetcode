class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        non_grumpy_sum = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                non_grumpy_sum += c
        print(non_grumpy_sum)

        init_sum = 0
        max_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                init_sum += customers[i]
        max_sum = init_sum
        
        # max_sum = 2
        # init_sum = 2
        # i = 4
        # pre_idx = 1
        # 
        
        for i in range(minutes, len(customers)):
            pre_idx = i - minutes
            if grumpy[pre_idx] == 1:
                init_sum -= customers[pre_idx]

            if grumpy[i] == 1:
                init_sum += customers[i]
            max_sum = max(max_sum, init_sum)

        # non_grumpy_sum = 10
        return non_grumpy_sum + max_sum
