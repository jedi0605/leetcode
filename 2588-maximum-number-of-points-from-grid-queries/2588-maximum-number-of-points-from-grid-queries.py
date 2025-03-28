class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        q = [(val, i) for i, val in enumerate(queries)]
        q.sort()
        visisted = set()
        res = [0] * len(queries)
        min_heap = [(grid[0][0], 0, 0)]
        visisted.add((0, 0))
        point = 0
        for limit, idx in q:
            while min_heap and min_heap[0][0] < limit:
                val, x, y = heappop(min_heap)
                point += 1
                direction = [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1),
                ]
                for d_x, d_y in direction:
                    if (
                        (d_x, d_y) not in visisted
                        and 0 <= d_x < ROWS
                        and 0 <= d_y < COLS
                    ):
                        heappush(min_heap, (grid[d_x][d_y], d_x, d_y))
                        visisted.add((d_x, d_y))
            res[idx] = point
        return res
