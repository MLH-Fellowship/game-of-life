import numpy as np
class Board:
    def __init__(self, filepath = None):
        self.board = []
        self.steps = 0
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

    def step(self):
        board = self.board
        self.steps += 1
        nboard = np.zeros((len(board), len(board[0])), dtype=int)
        for row in range(len(board)):
            for col in range(len(board[0])):
                #print("step",board)
                neighbours = self.count_neighbours(row, col)
                print(neighbours)
                if board[row][col] == 1 and (neighbours == 2 or neighbours == 3):  # noqa
                    nboard[row][col] = 1  # survivial

                if board[row][col] == 0 and neighbours == 3:
                    nboard[row][col] = 1  # birth
        board = nboard
        self.board = board
        return board



    def count_neighbours(self, i, j):
        m = len(self.board)
        n = len(self.board[0])
        live = 0
        for row in range(max(0, i - 1), min(i + 1, m - 1) + 1):
            for column in range(max(0, j - 1), min(j + 1, n - 1) + 1):
                live += (int(self.board[row][column])) & 1
        live -= int(self.board[i][j]) & 1
        return live

    def stats(self):
        alive = sum([sum(row) for row in self.board])
        dead = len(self.board)*len(self.board[0]) - alive
        stats = {
            'steps': self.steps,
            'alive cells': alive,
            'dead_cells': dead
        }
        return stats



def main():
    board = Board()
    board.display()
    board = Board('./myfile.txt')
    board.display()
    for i in range(10):
        board.step()
        #print(board.stats())


if __name__ == '__main__':
    main()