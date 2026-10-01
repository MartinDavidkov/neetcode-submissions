class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row logic
        for row in board:
            line =[char for char in row if char != "."]
            if len(line) != len(set(line)):
                return False

        #column logic
        for i in range(len(board)):
            column=[]
            for row in board:
                if row[i] != ".":
                    column.append(row[i])

            if len(column) != len(set(column)):
                return False

        #square logic
        start=0
        end=3
        for box_row in [0,3,6]:
            for box_column in [0,3,6]:
                square=[]
                for i in range(box_row, box_row+3):
                    for j in range(box_column, box_column+3):
                        if board[i][j] != ".":
                            square.append(board[i][j])
                if len(square) != len(set(square)):
                    return False

        return True