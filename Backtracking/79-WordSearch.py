from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if len(word) == 0:
        return True

    def backtrack(index, row, col):
        if index == len(word):
            return True

        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or word[index] != board[row][col]
        ):
            return False

        recover = board[row][col]
        board[row][col] = -1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if backtrack(index + 1, dr, dc):
                return True

        board[row][col] = recover
        return False

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == word[0]:
                if backtrack(0, i, j):
                    return True

    return False


testboard = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
testword = "ABCCED"
print(exist(testboard, testword))
