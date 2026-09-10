class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        board = [['.'] * n for _ in range(n)]

        # Track columns and both diagonal directions containing queens.
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row: int) -> None:
            if row == n:
                results.append([''.join(board_row) for board_row in board])
                return

            for col in range(n):
                if (
                    col in columns
                    or row + col in positive_diagonals
                    or row - col in negative_diagonals
                ):
                    continue

                board[row][col] = 'Q'
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                backtrack(row + 1)

                # Undo the choice before trying the next column.
                board[row][col] = '.'
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)
        return results
