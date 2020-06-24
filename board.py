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

    def see_neighbours(self):
        neighbours = []
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                is_neighbour = True
                #check each diretions 
        return neighbours
    def update_board(self):
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                #check the neighbours each time 
                get_neighbour = self.see_neighbours
                #collect living cells 
                cells_alive = []
                #look through array 
                for neighbour in get_neighbour:
                    if neighbour.lives() 
                        cells_alive.append(neighbour)





        
        

def main():
    board = Board()
    board.display()
    board = Board('./myfile.txt')
    board.display()

if __name__ == '__main__':
    main()
