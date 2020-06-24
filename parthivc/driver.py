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

    def display(self):
        print()
        for line in self.board:
            for elem in line:
                print(elem, end=" ")
            print()

    def getNeighborCount(self, x, y):
        count = 0
        for index in range(8):
            newX, newY = x + xList[index], y + yList[index]
            if self.inBounds(newX, newY) and self.board[newX][newY]:
                count += 1
        return count

    def inBounds(self, x, y):
        return -1 < x < self.rows and -1 < y < self.cols

    def step(self):
        stepped = list(map(list, self.board))
        for x in range(self.rows):
            for y in range(self.cols):
                count = self.getNeighborCount(x, y)
                if count == 3:
                    stepped[x][y] = 1
                elif count != 2 and self.board[x][y]:
                    stepped[x][y] = 0
        if self.board == stepped:
            return False
        self.board = stepped
        return True


def main():
    fileBoard = Board(0, 0, "board2.txt")
    fileBoard.display()
    while fileBoard.step():
        fileBoard.display()
    fileBoard.display()


if __name__ == '__main__':
    main()
