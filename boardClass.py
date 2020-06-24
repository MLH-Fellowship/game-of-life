
class Board:
    board = []
    numRows = 0
    numCols = 0

    # initializes board using a text file
    def __init__(self, filepath = None):
        if filepath:
            with open(filepath) as fp:
                lines = fp.readlines()
                for line in lines:
                    numRows += 1 
                    line = line.strip()
                    col = []
                    for c in line:
                        col.append(c)
                    numCols = col.len()
                    self.board.append(col)

    # display board's current state
    def display(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.board[row][col])
            print('\n')

    def sumNeighbours(self, row, col):
        # compute 8-neghbor sum using toroidal boundary conditions - x and y wrap around  
        sum = this.board[(row - 1) % numRows][(col - 1) % numCols] + this.board[(row - 1) % numRows][col] + this.board[(row - 1) % numRows][(col + 1) % numCols] + this.board[row][(col - 1) % numCols] + this.board[row][(col + 1) % numCols] + this.board[(row + 1) % numRows][(col - 1) % numCols] + this.board[(row + 1) % numRows][col] + this.board[(row + 1) % numRows][(col + 1) % numCols]
        return sum


    def step(self):
        # iterate through this.board in row major order
        for row in range(self.numRows):
            for col in range(self.numCols):
                
                state = sum(self, row, col)

                if self.board[row][col] == 1: # alive
                    # check if it has either 2 or 3 live neighbours
                    if state == 2 | state == 3:
                        pass
                    else 
                        col = 0
                else: # dead
                    # check if it has 3 live neighbours
                    if state == 3:
                        col = 1

