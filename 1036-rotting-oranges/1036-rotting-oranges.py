class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [[1, 0], [-1, 0], [0, 1],[0, -1]]
        queue = deque()
        visited = set()
        left_o = set()
        step = -1
        # init part, find 2 add to queue
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    left_o.add((r, c))
        if len(left_o) == 0:
            return 0
        # BFS
        while queue:
            print(len(queue))
            for _ in range(len(queue)):
                cur_r, cur_c = queue.popleft()
                for d_r, d_c in direction:
                    n_r, n_c = cur_r + d_r, cur_c + d_c
                    if (
                        0 <= n_r < row
                        and 0 <= n_c < col
                        and grid[n_r][n_c] == 1
                        and (n_r, n_c) not in visited
                    ):
                        queue.append((n_r, n_c))
                        grid[n_r][n_c] = 2
                        visited.add((n_r, n_c))
                        left_o.remove((n_r, n_c))
            print(grid)

            step+=1
        # check left_o
        print(left_o)
        if len(left_o) == 0:
            return step
        else:
            return -1
        