class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Edge cases
        if not board:
            return False
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        rows = {key: set() for key in range (0,9)}
        cols = {key: set() for key in range (0,9)}
        blocks = {(row,col): set() for row in range (0,3) for col in range(0,3)}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not ('1' <= board[i][j] <= '9' or board[i][j] == '.'):
                    return False
                if '1' <= board[i][j] <= '9':
                    if board[i][j] in rows[i].union(cols[j]).union(blocks[(i//3,j//3)]):
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3,j//3)].add(board[i][j])
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku(
    [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

