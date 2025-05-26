class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        maps = defaultdict(int) # ratio cnt
        res = 0
        for w,h in rectangles:
            r = w/h
            res += maps[r]
            maps[r]+=1
        return res