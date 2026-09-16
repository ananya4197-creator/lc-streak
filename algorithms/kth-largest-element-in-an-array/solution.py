class Solution:
    def solveNQueens(self, n):
        result = []

        # Create empty board
        board = [["."] * n for _ in range(n)]

        def isSafe(row, col):
            # Check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(row):
            # All queens placed
            if row == n:
                solution = []

                for i in range(n):
                    solution.append("".join(board[i]))

                result.append(solution)
                return

            # Try every column
            for col in range(n):

                if isSafe(row, col):

                    # Place queen
                    board[row][col] = "Q"

                    # Move to next row
                    solve(row + 1)

                    # Backtrack
                    board[row][col] = "."

        solve(0)

        return result