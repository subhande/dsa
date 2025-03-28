# N Queens

# from typing import List
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         pass

class Solution:
    # Check if it's safe to place a queen at board[row][col]
    def safe(self, board, row, col):
        r, c = row, col

        # Check upper left diagonal
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Reset to the original position
        r, c = row, col

        # Check left side
        while c >= 0:
            if board[r][c] == 'Q':
                return False
            c -= 1

        # Reset to the original position
        r, c = row, col

        # Check lower left diagonal
        while r < len(board) and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        # If no queens are found, it's safe
        return True

    # Function to place queens on the board
    def func(self, col, ans, board):
        # If all columns are filled, add the solution to the answer
        if col == len(board):
            ans.append(list(board))
            return

        # Try placing a queen in each row for the current column
        for row in range(len(board)):
            # Check if it's safe to place a queen
            if self.safe(board, row, col):
                # Place the queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]

                # Recursively place queens in the next columns
                self.func(col + 1, ans, board)

                # Remove the queen and backtrack
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    # Solve the N-Queens problem
    def solveNQueens(self, n):
        # List to store the solutions
        ans = []
        # Initialize the board with empty cells
        board = ["." * n for _ in range(n)]

        # Start placing queens from the first column
        self.func(0, ans, board)
        return ans

# Main method to test the solution
if __name__ == "__main__":
    solution = Solution()
    n = 4 # Example with 4 queens
    solutions = solution.solveNQueens(n)

    # Print all solutions
    for sol in solutions:
        for row in sol:
            print(row)
        print()
