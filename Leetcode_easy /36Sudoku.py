'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

'''
        
        
        
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            valid = {}
            valid2 = {}
            for j in range(9):
                if board[i][j] in valid:
                    return False
                elif board[i][j] != '.':
                    valid[board[i][j]] = 1
                
                if board[j][i] in valid2:
                    return False
                elif board[j][i] != '.':
                    valid2[board[j][i]] = 1
        
        for i in range(9):
            if i%3 == 0:
                 valid = {}
                 valid2 = {}
                 valid3 = {}
            for j in range(3):
                 if board[i][j] in valid:
                    return False
                 elif board[i][j] != '.':
                    valid[board[i][j]] = 1
            
            for j in range(3,6):
                 if board[i][j] in valid2:
                    return False
                 elif board[i][j] != '.':
                    valid2[board[i][j]] = 1  
                    
            for j in range(6,9):
                 if board[i][j] in valid3:
                    return False
                 elif board[i][j] != '.':
                    valid3[board[i][j]] = 1  
       
        
        return True    
                
                        