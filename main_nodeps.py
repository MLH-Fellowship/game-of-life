import sys

import board


def main(state_file):
    life = board.Board(state_file)
    life.display()


if __name__ == '__main__':
    main(sys.argv[1])
