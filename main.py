import boardClass


def main(filepath):
    life = boardClass.Board(filepath)
    for i in range(3):
        life.display()
        life.step()
    

if __name__ == '__main__':
    main("./board.txt")