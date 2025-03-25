class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [[x[0], x[2]] for x in rectangles]
        y = [[x[1], x[3]] for x in rectangles]
        x.sort()
        y.sort()

        def can_cut(intervals):
            count = 0
            res = []
            cur = [intervals[0][0], intervals[0][1]]
            for i in intervals:
                if i[0] < cur[1]:  # merge
                    cur[1] = max(cur[1], i[1])
                else:
                    res.append(cur.copy())
                    cur[0], cur[1] = i[0], i[1]
            res.append(cur)
            return len(res)
        x_c = can_cut(x)
        y_c = can_cut(y)
        return max(x_c,y_c) >=3

# 3169
