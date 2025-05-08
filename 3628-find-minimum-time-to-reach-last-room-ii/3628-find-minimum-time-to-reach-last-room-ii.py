class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        # array for remember smallest time
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # time, i, j
        visited = set()

        while heap:
            cur_time, cur_i, cur_j = heappop(heap)
            visited.add((cur_i, cur_j))
            if cur_i == m - 1 and cur_j == n - 1:
                return cur_time

            for n_r, n_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = cur_i + n_r, cur_j + n_c
                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and dist[new_row][new_col] == float("inf")
                ):
                    new_condition = (cur_i + cur_j) % 2
                    next_time = (
                        max(moveTime[new_row][new_col], cur_time) + new_condition + 1
                    )
                    if next_time < dist[new_row][new_col]:
                        dist[new_row][new_col] = next_time
                        heappush(heap, (next_time, new_row, new_col))
        return 0
