# Created by Parthiv Chigurupati

import os


class Board:

    def __init__(self, fName=None):
        self.board = [[0] * 8] * 8
        self.change = [[0] * 8] * 8
        if fName:
            self.getBoardFromFile(fName)

    def getBoardFromFile(self, fName):
        if os.path.isfile(fName) and fName.endswith(".txt"):
            file = open(fName, "r+")
            for index, line in enumerate(file.readlines()):
                try:
                    data = list(map(int, [char for char in line][:-1]))
                    self.board[index] = data
                except ValueError:
                    print("File contains invalid data, aborting file read now")
                    return
            file.close()
        else:
            print("Invalid file path")

    def display(self):
        print()
        for line in self.board:
            for elem in line:
                print(elem, end=" ")
            print()
        print()


def main():
    game = Board()
    game.display()
    fileBoard = Board("board.txt")
    fileBoard.display()


if __name__ == '__main__':
    main()
