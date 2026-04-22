class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num = ["1","2","3","4","5","6","7","8","9"]
        for i in range(0,9):
            for j in num:
                if board[i].count(j) > 1:
                    return False
        
        for i in range(0,9):
            cols = []
            for j in range(0,9):
                cols.append(board[j][i])
            for k in num:
                if cols.count(k) > 1:
                    return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                for i in num:
                    if box.count(i) > 1:
                        return False

        
        
        return True
        
