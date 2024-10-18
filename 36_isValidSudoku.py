from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row level validation
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[r][c]
                if item in s:
                    return False
                if item != ".":
                    s.add(item)

        # col level validation
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[c][r]
                if item in s:
                    return False
                if item != ".":
                    s.add(item)

        # box level validation
        starts = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]
        for r, c in starts:
            s = set()
            for row in range(r, r + 3):
                for col in range(c, c + 3):
                    item = board[row][col]
                    if item in s:
                        return False
                    if item != ".":
                        s.add(item)

        return True


ss = Solution()

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(ss.isValidSudoku(board))
