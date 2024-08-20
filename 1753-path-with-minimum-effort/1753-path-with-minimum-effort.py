class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # using BFS and Heap
        ROW, COL = len(heights), len(heights[0])
        heap = [[0, 0, 0]]  # diff, row, col
        visit = set()

        while heap:
            diff, c_row, c_col =heappop(heap)            
            if c_row == ROW -1 and c_col == COL-1:
                return diff
            if (c_row,c_col) in visit:
                continue
            visit.add((c_row, c_col))
            
            DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d_r, d_c in DIR:
                new_r, new_c = c_row + d_r, c_col + d_c
                if new_r < 0 or new_c < 0 or new_c == COL or new_r == ROW:
                    continue
                if (new_r, new_c) in visit:
                    continue
                new_diff = 0
                new_diff = max(diff, abs(heights[c_row][c_col] - heights[new_r][new_c]))
                heappush(heap,(new_diff,new_r,new_c))