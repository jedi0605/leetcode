class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRT = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(heights), len(heights[0])
        heap = [[0, 0, 0]]  # diff row col
        visit = set()

        while heap:
            diff, c_r, c_c = heappop(heap)
            if c_r == ROW - 1 and c_c == COL - 1:
                return diff
            if (c_r, c_c) in visit:
                continue
            visit.add((c_r, c_c))
            for d_r, d_c in DIRT:
                n_r, n_c = c_r + d_r, c_c + d_c
                if (
                    n_r < 0
                    or n_c < 0
                    or n_r == ROW
                    or n_c == COL
                    or (n_r, n_c) in visit
                ):
                    continue
                new_diff = max(diff, abs(heights[n_r][n_c] - heights[c_r][c_c]))
                heappush(heap, [new_diff,n_r,n_c])