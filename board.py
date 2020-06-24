class Board:
    def __init__(self, filepath = None):
        self.board = []
        if filepath:
            with open(filepath) as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.strip()
                    self.board.append([c for c in line])

    def display(self):
        r = len(self.board)
        c = 0 if r < 1 else len(self.board[0])
        for i in range(r):
            for j in range(c):
                print(self.board[i][j], end='')
            print()
        return

    #define main loop, step function 

    def see_neighbors(self, b_row, b_column):
        neighbors = [] #neighbors we will return
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                is_valid_neighbor = True
                #check each diretions 
                next_row = row + b_row
                next_column = column + b_column
                
                if (next_row < 0) or (next_row >= len(self.board)):
                    is_valid_neighbor = false
                if (next_column < 0) or (next_row >= len(self.board[0])):
                    is_valid_neighbor = false
                if (next_row < 0) or (next_row >= len(self.board)):
                    is_valid_neighbor = false
                if (is_valid_neighbor):
                    neighbors.append(self.board[next_row][next_column])

                #check within parameters 
        return neighbors
    def update_board(self):
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                    #check the neighbors each time 
                    get_neighbor = self.see_neighbors(row,column)
                    #collect living cells 
                    cells_alive = []
                    #look through array 
                    for neighbor in get_neighbor:
                        if neighbor.lives():
                            cells_alive.append(neighbor)





        
        

def main():
    board = Board()
    board.display()
    board = Board('./myfile.txt')
    board.display()

if __name__ == '__main__':
    main()
