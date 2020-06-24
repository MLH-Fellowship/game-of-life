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

    def alive_neighbors(self,row,col):
        # Add padded border of zeros (to get rid of edge cases)
        shape = self.board.shape
        temp_board = np.zeros((shape[0] + 2, shape[1] + 2),dtype=int)
        temp_board[1:shape[0]+1,1:shape[1]+1] = self.board[0:shape[0],0:shape[1]]
        
        # Account for new shape
        row += 1
        col += 1
        
        # Count number of alive neighbors
        alive = 0
        alive += temp_board[row - 1, col]
        alive += temp_board[row + 1, col]
        alive += temp_board[row, col - 1]
        alive += temp_board[row, col + 1]
        alive += temp_board[row - 1, col - 1]
        alive += temp_board[row + 1, col + 1]
        alive += temp_board[row - 1, col + 1]
        alive += temp_board[row + 1, col - 1]
        
        return alive
    
    def step(self):
        rows,cols = self.board.shape

        new_board = np.copy(self.board) # need to keep old board to prevent updates from affecting decisions
        for row in range(rows):
            for col in range(cols):
                alive = self.alive_neighbors(row,col)
                if self.board[row,col] == 0:
                    if alive == 3:
                        new_board[row,col] = 1
                else:
                    if alive != 2 and alive != 3:
                        new_board[row,col] = 0
                    
        self.board = np.copy(new_board)

def main(filename):
    x = Board(filename)

    while True:
        print("BOARD: ")
        x.display()
        input()
        x.step()

'''
if __name__ == "__main__":
    x = Board('test.txt')
    x.display()
    x.step()
    print()
    x.display()
'''
