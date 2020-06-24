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


def main():
    board = Board()
    board.display()
    board = Board('./myfile.txt')
    board.display()

if __name__ == '__main__':
    main()