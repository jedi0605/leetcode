class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0

        init_sum = sum( calories[:k])
        if init_sum < lower:
            res -=1
        if init_sum > upper:
            res+=1
        for i in range(k,len(calories)):
            pre_num = calories[i-k]
            init_sum -= pre_num
            init_sum+=calories[i]
            if init_sum < lower:
                res -=1
            if init_sum > upper:
                res+=1
        return res