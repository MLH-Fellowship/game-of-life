import os


class GameOfLife:
    def __init__(self):
        self.board = []
        with open('input.txt') as f:
            board = f.readlines()
        for row in board:
            self.board.append([c for c in row.strip()])

    def display(self):
        return '\n'.join([''.join(row) for row in self.board])
