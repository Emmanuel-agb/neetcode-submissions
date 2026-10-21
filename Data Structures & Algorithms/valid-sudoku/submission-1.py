class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []  # Store each filled cell's row, column, and 3x3 box information

        # Traverse all 9 rows and 9 columns
        for i in range(9):
            for j in range(9):
                element = board[i][j] # Get the current cell's value
                # Ignore empty cells because only filled cells need validation
                if element != '.':
                    # Record the digit with its row and column
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        
        # If every record is unique, no digit violates any Sudoku rule
        # A set removes duplicates, so equal lengths mean there are none
        return len(res) == len(set(res))