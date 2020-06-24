import numpy as np

class Board:
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.readlines()

            if lines == []:
                print("Empty board")

            lines = [line.strip() for line in lines] # remove newline character from each line
            rows = len(lines)
            cols = len(lines[0])

            self.board = np.zeros([rows,cols],dtype=int)

            for row, line in enumerate(lines):
                for col in range(cols):
                    self.board[row,col] = int(line[col])
                    
        
    def display(self):
        for row in self.board:
            for val in row:
                print(val, end="")
            print('\n')
    
