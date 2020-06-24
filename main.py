import board


def main(filepath):
    life = board.Board(filepath)
    while True:
        life.display()
        life.step()

if __name__ == '__main__':
    main()