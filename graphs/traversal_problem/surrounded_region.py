# Sorrounded Regions


from collections import deque
from typing import List

class Solution:

    def isValid(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols

    def bfs(self, r, c, rows, cols, board):
        queue = deque()
        queue.append((r, c))
        board[r][c] = "E"

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr = row + dr
                nc = col + dc
                if self.isValid(nr, nc, rows, cols) and board[nr][nc] == "O":
                    queue.append((nr, nc))
                    board[nr][nc] = "E"

    def solve(self, board: List[List[str]]):
        if not board or not board[0]:
            return -1
        rows, cols = len(board), len(board[0])
        border_cells = [(0,i) for i in range(cols)]
        border_cells += [(rows-1,i) for i in range(cols)]
        border_cells += [(i,0) for i in range(1, rows-1)]
        border_cells += [(i,cols-1) for i in range(1, rows-1)]

        for row, col in border_cells:
            if board[row][col] == "O":
                self.bfs(row, col, rows, cols, board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # captured
                elif board[r][c] == "E":
                    board[r][c] = "O"  # escaped
