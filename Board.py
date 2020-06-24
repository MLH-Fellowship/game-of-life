
class Board (object):

        def __init__(self, file):
            self.board = []
            for i in f:
                row = []
                for j in list(i):
                    if (j.isdigit()):
                        row.append(int(j))
                self.board.append(row)

        def display(self):
            for i in self.board:
                print(*i)

if __name__=="__main__":
    f = open("test.txt", "r")
    b = Board(f)
    b.display()
