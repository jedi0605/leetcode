class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            res.append(newInterval)
            return res
        
        for idx, inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
                res.append([inter[0], inter[1]])
            elif inter[0] > newInterval[1]:
                res.append(newInterval)
                res = res + intervals[idx:]
                return res
            else:
                newInterval[0] = min(newInterval[0], inter[0])
                newInterval[1] = max(newInterval[1], inter[1])
        res.append(newInterval)
        return res
