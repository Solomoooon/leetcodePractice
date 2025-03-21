from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    # Function to check if placing a queen is valid
    def isValid(board, row, col):
        # Check the same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check upper right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == "Q":
                return False

        return True

    # Backtracking function
    def backtrack(board, row):
        if row == n:
            # Convert the current board to a list of strings and add to results
            results.append(["".join(r) for r in board])
            return

        for col in range(n):
            if isValid(board, row, col):
                # Place the queen
                board[row][col] = "Q"
                backtrack(board, row + 1)  # Recurse to the next row
                # Backtrack: Remove the queen
                board[row][col] = "."

    # Initialize the board and results
    board = [["." for _ in range(n)] for _ in range(n)]  # Correct initialization
    results = []
    backtrack(board, 0)  # Start from the first row
    return results
