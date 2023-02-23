# BAD!! NEED TO RETHINK!
# BAD!! NEED TO RETHINK!
# BAD!! NEED TO RETHINK!
# BAD!! NEED TO RETHINK!
# BAD!! NEED TO RETHINK!
# BAD!! NEED TO RETHINK!


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not self.check_lines(board):
            return False

        transpon_board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                transpon_board[j][i] = board[i][j]

        if not self.check_lines(transpon_board):
            return False

        boxes3x3 = []
        line1 = []
        line2 = []
        line3 = []
        for line in board[0:3]:
            for value_idx in range(len(line)):
                if value_idx <= 2:
                    line1.append(line[value_idx])
                elif value_idx <= 5:
                    line2.append(line[value_idx])
                else:
                    line3.append(line[value_idx])

        boxes3x3.append(line1)
        boxes3x3.append(line2)
        boxes3x3.append(line3)

        line4 = []
        line5 = []
        line6 = []
        for line in board[3:6]:
            for value_idx in range(len(line)):
                if value_idx <= 2:
                    line4.append(line[value_idx])
                elif value_idx <= 5:
                    line5.append(line[value_idx])
                else:
                    line6.append(line[value_idx])

        boxes3x3.append(line4)
        boxes3x3.append(line5)
        boxes3x3.append(line6)

        line7 = []
        line8 = []
        line9 = []
        for line in board[6:]:
            for value_idx in range(len(line)):
                if value_idx <= 2:
                    line7.append(line[value_idx])
                elif value_idx <= 5:
                    line8.append(line[value_idx])
                else:
                    line9.append(line[value_idx])

        boxes3x3.append(line7)
        boxes3x3.append(line8)
        boxes3x3.append(line9)

        if not self.check_lines(boxes3x3):
            return False

        return True

    def check_lines(self, lines):
        for line in lines:
            new_set = set()
            for value in line:
                if value == ".":
                    continue
                if value not in new_set:
                    new_set.add(value)
                else:
                    return False
        return True


s = Solution()
# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"],
# ]

# print(s.isValidSudoku(board=board))

# board2 = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# print(s.isValidSudoku(board=board2))


board3 = [
    [".",".",".",".",".",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    ["9","3",".",".","2",".","4",".","."],
    [".",".","7",".",".",".","3",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","3","4",".",".",".","."],
    [".",".",".",".",".","3",".",".","."],
    [".",".",".",".",".","5","2",".","."],
]

print(s.isValidSudoku(board=board3))