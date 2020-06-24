
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
                    self.numRows += 1 
                    line = line.strip()
                    col = []
                    for c in line:
                        col.append(c)
                    self.numCols = len(col)
                    self.board.append(col)

    # display board's current state
    def display(self):
        print("\n")
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.board[row][col], end =" ")
            print("")

    def sumNeighbours(self, row, col):
        # compute 8-neghbor sum using toroidal boundary conditions - x and y wrap around  
        sum = int(self.board[(row - 1) % self.numRows][(col - 1) % self.numCols]) + int(self.board[(row - 1) % self.numRows][col]) + int(self.board[(row - 1) % self.numRows][(col + 1) % self.numCols]) + int(self.board[row][(col - 1) % self.numCols]) + int(self.board[row][(col + 1) % self.numCols]) + int(self.board[(row + 1) % self.numRows][(col - 1) % self.numCols]) + int(self.board[(row + 1) % self.numRows][col]) + int(self.board[(row + 1) % self.numRows][(col + 1) % self.numCols])
        return sum


    def step(self):
        # iterate through self.board in row major order
        for row in range(self.numRows):
            for col in range(self.numCols):
                
                state = self.sumNeighbours(row, col)
                #print(state)

                if self.board[row][col] == 1: # alive
                    # check if it has either 2 or 3 live neighbours
                    if state == 2 | state == 3:
                        pass
                    else:
                        print("updated alive -> alive using neighbour sum: ", state)
                        self.board[row][col] = 0
                else: # dead
                    # check if it has 3 live neighbours
                    if state == 3:
                        print("updated dead -> alive using neighbour sum: ", state)
                        self.board[row][col] = 1

