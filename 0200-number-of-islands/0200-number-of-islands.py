class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        islandCnt = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                islandCnt += 1
                queue = deque()
                queue.append((r, c))
                visited.add((r, c))
                while queue:
                    c_r, c_c = queue.popleft()
                    for n_r, n_c in direction:
                        if (
                            0 <= c_r + n_r < len(grid)
                            and 0 <= c_c + n_c < len(grid[0])
                            and (c_r + n_r, c_c + n_c) not in visited
                            and grid[c_r + n_r][c_c + n_c] == "1"
                        ):
                            queue.append((c_r + n_r, c_c + n_c))
                            visited.add((c_r + n_r, c_c + n_c))
        return islandCnt