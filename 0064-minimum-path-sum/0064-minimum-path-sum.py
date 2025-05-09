class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Dijkstra's Algorithm version
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        min_sum = [[float("inf")] * n for _ in range(m)]
        # print(min_sum)

        while heap:
            cur_sum, cur_r, cur_l = heappop(heap)
            if (cur_r, cur_l) == (m - 1, n - 1):
                return cur_sum
            for new_r, new_c in [
                (cur_r + 1, cur_l),
                # (cur_r - 1, cur_l),
                (cur_r, cur_l + 1)
                # (cur_r, cur_l - 1),
            ]:
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_sum = cur_sum + grid[new_r][new_c]
                    if new_sum < min_sum[new_r][new_c]:
                        heappush(heap, (new_sum, new_r, new_c))
                        min_sum[new_r][new_c] = new_sum
        return res

        # pre = 0
        # for i in range(len(grid[0])):
        #     grid[0][i] += pre
        #     pre = grid[0][i]
        # pre = 0
        # for i in range(len(grid)):
        #     grid[i][0] += pre
        #     pre = grid[i][0]

        # for i in range(1, len(grid)):
        #     for j in range(1, len(grid[0])):
        #         grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # return grid[-1][-1]
