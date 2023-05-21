# 36. Valid Sudoku Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

from ast import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                if cell in rows[r]:
                    return False
                if cell in cols[c]:
                    return False
                if cell in squares[(r//3, c//3)]:
                    return False                
                cols[c].add(cell)
                rows[r].add(cell)
                squares[(r//3, c//3)].add(cell)
        return True