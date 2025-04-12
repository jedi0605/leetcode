class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, idx):
            if (
                r < 0
                or r == len(board)
                or c < 0
                or c == len(board[0])
                or board[r][c] != word[idx]
            ):
                return False
            if idx == len(word) - 1:
                return True
            tmp = board[r][c]
            board[r][c] = "."
            found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )
            board[r][c] = tmp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
