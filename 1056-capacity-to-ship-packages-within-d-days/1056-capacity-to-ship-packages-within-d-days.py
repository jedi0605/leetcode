class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # def work(cap: int) -> bool:
        #     curTotal = 0
        #     dayNeeds = 1
        #     for w in weights:
        #         if curTotal + w > cap:
        #             curTotal = w
        #             dayNeeds += 1
        #         else:
        #             curTotal += w
        #     return dayNeeds <= days
        def work(cap:int) -> bool:
            work_d = 1
            cur_w = 0
            for w in weights:
                if cur_w + w > cap:
                    work_d+=1
                    cur_w = w
                else:
                    cur_w+=w
            return work_d<=days
        work(7)
        l,r = max(weights), sum(weights)
        while l<r:
            mid = (l+r) // 2
            if work(mid) == False:
                l = mid +1
            else:
                r = mid
        print(f"{l}, {r}")
        return l
