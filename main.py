import fire

import board


def main(state_file):
    life = board.Board(state_file)
    while True:
        life.display()
        life.update()
        input('')


if __name__ == '__main__':
    fire.Fire(main)
