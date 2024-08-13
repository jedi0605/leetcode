class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.max_of_weights = max(weights)

        def work(cap: int) -> bool:
            curTotal = 0
            dayNeeds = 1
            for w in weights:
                if curTotal + w > cap:
                    curTotal = w
                    dayNeeds += 1
                else:
                    curTotal += w
            return dayNeeds <= days
            # tmp = weights[:]
            # # if cap < self.max_of_weights:
            # #     return False
            # for d in range(days):
            #     cap_tmp = cap
            #     for i in range(len(tmp)):
            #         if cap_tmp >= tmp[i]:
            #             cap_tmp -= tmp[i]
            #             tmp[i] = 0
            # return sum(tmp) == 0

        l = self.max_of_weights
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2
            if work(mid) == False:
                l = mid + 1
            else:
                r = mid

        return l
