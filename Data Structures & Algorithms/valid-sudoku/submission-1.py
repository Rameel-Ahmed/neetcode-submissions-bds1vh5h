class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicate(x:List):
            seen = {}
            for num in x:
                if num in seen:
                    return True
                if num==".":
                    pass
                else:
                    seen[num]=0
            return False


        # Check rows
        for row in board:
            if has_duplicate(row):
                return False

        # Check columns
        for col in range(9):
            column = []

            for row in range(9):
                column.append(board[row][col])

            if has_duplicate(column):
                return False

        # Check each 3 × 3 box
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                box = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        box.append(board[row][col])

                if has_duplicate(box):
                    return False

        return True