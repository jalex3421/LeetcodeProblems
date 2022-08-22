
class Solution:
    def isValidSudoku(self, board):
        return (self.rowValidation(board) and self.columnValidation(board) and self.subgridValidation(board))

    def rowValidation(self, board):
        for row in board:
            if self.isSubsetValid(row) != True:
                return False
        return True

    def columnValidation(self, board):
        for col in zip(*board):
            if self.isSubsetValid(col) != True:
                return False
        return True

    def subgridValidation(self, board):
        #these are the index from the subgrids
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                #define the subgrid
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if self.isSubsetValid(subgrid) !=True:
                    return False
        return True

    def isSubsetValid(self, subset):
        subset = [i for i in subset if i != '.']
        #return comparison between lengths
        return (len(set(subset)) == len(subset))

    
