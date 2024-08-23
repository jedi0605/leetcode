class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW, COL = len(heights), len(heights[0])
        heap = [[0, 0, 0]]  # diff, row, COL
        visit = set()
        DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while heap:
            diff, c_r, c_l = heappop(heap)
            if c_r == ROW - 1 and c_l == COL - 1:
                return diff
            if (c_r, c_l) in visit:
                continue
            visit.add((c_r, c_l))
            for r, l in DIR:
                new_r = c_r + r
                new_l = c_l + l
                # if 0 <= new_r < ROW == False and 0 <= new_l < COL == False:
                #     continue
                if (
                    new_r < 0
                    or new_l < 0
                    or new_r == ROW
                    or new_l == COL
                    or (new_r, new_l) in visit
                ):
                    continue
                print(f"{new_r},{new_l}")
                cur_diff = max(diff, abs(heights[c_r][c_l] - heights[new_r][new_l]))
                heappush(heap, (cur_diff, new_r, new_l))
