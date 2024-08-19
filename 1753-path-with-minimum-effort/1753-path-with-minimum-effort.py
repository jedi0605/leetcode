class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW, COL = len(heights), len(heights[0])
        heap = [[0, 0, 0]]  # diff, row, col
        visit = set()
        dirt = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while heap:
            diff, cr, cc = heappop(heap)
            if cr == ROW - 1 and cc == COL - 1:
                return diff
            if (cr,cc) in visit:
                continue
            visit.add((cr, cc))
            for dirt_r, dirt_c in dirt:
                new_r, new_c = cr + dirt_r, cc + dirt_c
                if new_r < 0 or new_c < 0 or new_r == ROW or new_c == COL:
                    continue
                if (new_r, new_c) in visit:
                    continue
                new_diff = max(diff, abs(heights[cr][cc] - heights[new_r][new_c]))
                heappush(heap, (new_diff, new_r, new_c))
