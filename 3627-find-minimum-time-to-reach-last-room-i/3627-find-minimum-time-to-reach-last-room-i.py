class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m) ] # array for remember smallest time
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # time, i, j
        visited = set()

        while heap:
            cur_time, cur_i, cur_j = heappop(heap)
            visited.add((cur_i, cur_j))
            if cur_i == m - 1 and cur_j == n - 1: return cur_time

            for n_r, n_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= cur_i + n_r < m and 0 <= cur_j + n_c < n:
                    if (cur_i + n_r, cur_j + n_c) not in visited:
                        next_time = (
                            max(moveTime[cur_i + n_r][cur_j + n_c], cur_time) + 1
                        )
                        if next_time < dist[cur_i + n_r][cur_j + n_c]:
                            dist[cur_i + n_r][cur_j + n_c]= next_time
                            heappush(heap, (next_time, cur_i + n_r, cur_j + n_c))
        return 0
