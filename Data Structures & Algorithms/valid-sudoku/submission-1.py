from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets
        col_set = defaultdict(set)
        row_set = defaultdict(set)        
        squares = defaultdict(set)

        # iterate
        for r in range(9):
            for c in range(9):
                # check for space -- skip
                if board[r][c] == '.':
                    continue
                if (board[r][c] in col_set[c] or 
                   board[r][c] in row_set[r] or 
                   board[r][c] in squares[r//3, c//3]):
                   return False
                
                # add 
                col_set[c].add(board[r][c])
                row_set[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True

    
    # we need to check columns, row, squares
    # if present in any then --> return false since duplicate
    # iterate through each row, col by col
