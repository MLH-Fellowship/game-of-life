class Board:
    def __init__(self, filepath):
        self.board = []
        with open(filepath) as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.strip()
                self.board.append([c for c in line])

    def display(self):
        r = len(self.board)
        c = len(self.board[0])
        for i in range(r):
            for j in range(c):
                print(self.board[i][j], end='')
            print()
        return


board = Board('./myfile.txt')
board.display()
