# Created by Parthiv Chigurupati

import os
import sys


xList = [-1, -1, -1, 0, 0, 1, 1, 1]
yList = [-1, 0, 1, -1, 1, -1, 0, 1]


class Board:

    def __init__(self, rows=None, cols=None, fName=None):
        if fName:
            self.board, self.rows, self.cols = self.getBoardFromFile(fName)
        elif rows and cols:
            self.board = [[0] * cols] * rows
            self.rows = rows
            self.cols = cols
        else:
            sys.exit("Invalid board initialization")
        self.change = self.board[:]

    @staticmethod
    def getBoardFromFile(fName):
        if os.path.isfile(fName) and fName.endswith(".txt"):
            file = open(fName, "r+")
            board = []
            for index, line in enumerate(file.readlines()):
                try:
                    data = list(map(int, [char for char in line.strip('\n')]))
                    board.append(data)
                except ValueError:
                    print("File contains invalid data, aborting file read now")
                    return
            file.close()
            return board, len(board), len(board[0])
        else:
            sys.exit("Invalid file path")

    def display(self, both=False):
        print()
        for line in self.board:
            for elem in line:
                print(elem, end=" ")
            print()
        if both:
            print()
            for line in self.change:
                for elem in line:
                    print(elem, end=" ")
                print()

    def getNeighborCount(self, x, y):
        count = 0
        for index in range(8):
            newX, newY = x + xList[index], y + yList[index]
            if self.inBounds(newX, newY) and self.board[newX][newY]:
                count += 1
        if count > 1:
            print(x, y, count)
        return count

    def inBounds(self, x, y):
        return -1 < x < self.rows and -1 < y < self.cols

    def step(self):
        for x in range(self.rows):
            for y in range(self.cols):
                count = self.getNeighborCount(x, y)
                if count == 3:
                    self.change[x][y] = 1
                elif count != 2 and self.board[x][y]:
                    self.change[x][y] = 0
        self.display(True)
        if self.board == self.change:
            return False
        self.board = self.change[:]
        return True


def main():
    # game = Board(8, 8)
    # game.display()
    fileBoard = Board(0, 0, "board.txt")
    fileBoard.display()
    while fileBoard.step():
        fileBoard.display()


if __name__ == '__main__':
    main()
