class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True

        def backtrack(index, row, col):
            if index == len(word):
                return True

            if (
                row < 0
                or row > len(board) - 1
                or col < 0
                or col > len(board[0]) - 1
                or word[index] != board[row][col]
            ):
                return False

            recover = board[row][col]

            board[row][col] = -1

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if backtrack(index + 1, row + dr, col + dc):
                    return True

            board[row][col] = recover
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    print("aa")
                    if backtrack(0, i, j):
                        print("aa")
                        return True

        return False
