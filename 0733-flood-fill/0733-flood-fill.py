class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        visit = set()
        start_c = image[sr][sc]

        def dfs(r, c):
            print(f"{r},{c}")
            if (
                r < 0
                or r == len(image)
                or c < 0
                or c == len(image[0]) or (r, c) in visit):
                return
            if image[r][c] != start_c:
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        for r, c in visit:
            image[r][c] = color

        return image
