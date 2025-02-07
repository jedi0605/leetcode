class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        new_s, new_e = intervals[0]
        res = []
        for s,e in intervals:
            if s > new_e:
                res.append([new_s,new_e])
                new_s, new_e = s,e
            else:
                new_s = min(new_s,s)
                new_e = max(new_e,e)
        res.append([new_s,new_e])
        return res