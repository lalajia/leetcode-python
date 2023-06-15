"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

import collections
from typing import List


# 创建一个和原本board一样的 然后用set横着比，竖着比，square 的比
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizental = [set() for _ in range(9)]
        vertical = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if (
                    board[i][j] in horizental[i]
                    or board[i][j] in vertical[j]
                    or board[i][j] in square[(i // 3) * 3 + (j // 3)]
                ):
                    return False
                horizental[i].add(board[i][j])
                vertical[j].add(board[i][j])
                square[(i // 3) * 3 + (j // 3)].add(board[i][j])

            # for num in board[i]:
            #     if num == ".":
            #         continue
            #     if num in horizental:
            #         return False
            #     horizental.add(num)
            # horizental.clear()

            # for num in board[0][i]:
            #     print(board[0][i])
            #     if num == ".":
            #         continue
            #     if num in vertical:
            #         return False
            #     vertical.add(num)
            # vertical.clear()
        return True

    def fromNeetcode(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


print(
    Solution().isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            ["3", ".", ".", "2", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
