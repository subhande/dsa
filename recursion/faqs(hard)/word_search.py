# Word Serach

from typing import List
class Solution:
    def backtrack(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = self.backtrack(board, word, i+1, j, index+1) or self.backtrack(board, word, i-1, j, index+1) or self.backtrack(board, word, i, j+1, index+1) or self.backtrack(board, word, i, j-1, index+1)
        board[i][j] = temp
        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.backtrack(board, word, i, j, 0):
                    return True
        return False
