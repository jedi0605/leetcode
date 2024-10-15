class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        queue = deque()
        visited = set()
        start_color = image[sr][sc]
        queue.append((sr, sc))
        dir_arr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            c_r, c_c = queue.popleft()
            if (c_r, c_c) in visited:
                continue

            for r, c in dir_arr:
                new_r, new_c = c_r + r, c_c + c
                if (
                    new_r < 0
                    or new_r == len(image)
                    or new_c < 0
                    or new_c == len(image[0])
                    or (new_r, new_c) in visited
                    or image[new_r][new_c] != start_color
                ):
                    continue
                else:
                    queue.append((new_r, new_c))
            
            visited.add((c_r, c_c))

        print(visited)
        for r,c in visited:
            image[r][c] = color
        return image
