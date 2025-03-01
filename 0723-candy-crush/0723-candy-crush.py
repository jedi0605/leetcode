class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Find three same i,j. Return set()
        def FindThreePair():
            output = set()
            # check row
            for i in range(1, len(board) - 1):
                for j in range(0, len(board[0])):
                    if board[i][j] == 0:
                        continue
                    if board[i - 1][j] == board[i][j] == board[i + 1][j]:
                        output.add((i - 1, j))
                        output.add((i, j))
                        output.add((i + 1, j))
            for i in range(len(board)):
                for j in range(1, len(board[0]) - 1):
                    if board[i][j] == 0:
                        continue
                    if board[i][j - 1] == board[i][j] == board[i][j + 1]:
                        output.add((i, j - 1))
                        output.add((i, j))
                        output.add((i, j + 1))
            return output

        # Mark set() to zero
        def Mark(markHash: set):
            for i, j in markHash:
                board[i][j] = 0

        # Drop down the candy
        def Drop():
            for c in range(len(board[0])):
                # last_zero = -1
                last_zero = len(board) - 1
                for r in range(len(board) - 1, -1, -1):
                    if board[r][c] != 0:
                        board[r][c], board[last_zero][c] = (
                            board[last_zero][c],
                            board[r][c],
                        )
                        last_zero -= 1

        markSet = FindThreePair()
        while markSet:
            Mark(markSet)
            Drop()
            markSet = FindThreePair()

        return board
