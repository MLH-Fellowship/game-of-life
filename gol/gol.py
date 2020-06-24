import numpy as np


class GameOfLife:
    def __init__(self):
        self.board = []
        self.steps = 0
        with open('input.txt') as f:
            board = f.readlines()
        for row in board:
            self.board.append([int(c) for c in row.strip()])
        self.board = np.array(self.board)

    def count_neighbours(self, i, j, board):
        """Returns sum of 8 immediate neighbours"""
        area = board[max(0, i - 1): min(len(board), i + 2),
                     max(0, j - 1): min(len(board[0]), j + 2)]
        return np.sum(area) - board[i, j]

    def step(self):
        board = self.board
        self.steps += 1
        nboard = np.zeros((len(board), len(board[0])), dtype=int)
        for row in range(len(board)):
            for col in range(len(board[0])):
                neighbours = self.count_neighbours(row, col, board)
                if board[row][col] == 1 and (neighbours == 2 or neighbours == 3):  # noqa
                    nboard[row][col] = 1  # survivial

                if board[row][col] == 0 and neighbours == 3:
                    nboard[row][col] = 1  # birth
        board = nboard
        self.board = board
        return board

    def stats(self):
        alive = sum([sum(row) for row in self.board])
        dead = len(self.board)*len(self.board[0]) - alive
        stats = {
            'steps': self.steps,
            'alive cells': alive,
            'dead_cells': dead
        }
        return stats

    def display(self):
        return '\n'.join([''.join([str(c) for c in row]) for row in self.board])  # noqa
