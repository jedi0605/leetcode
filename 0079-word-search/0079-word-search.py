class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx):
            if (
                row < 0
                or col < 0
                or row == len(board)
                or col == len(board[0])
                or board[row][col] == "."
                or board[row][col] != word[idx]
            ):
                return False
            if idx == len(word) - 1:
                return True
            tmp = board[row][col]
            board[row][col] = "."
            found = (
                dfs(row + 1, col, idx + 1)
                or dfs(row - 1, col, idx + 1)
                or dfs(row, col + 1, idx + 1)
                or dfs(row, col - 1, idx + 1)
            )
            board[row][col] = tmp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
