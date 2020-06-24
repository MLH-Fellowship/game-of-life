import time


class Board:
    def __init__(self, filepath=None):
        self.__state = []
        if filepath:
            with open(filepath) as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.strip()
                    self.__state.append([c for c in line])
        self.size = [len(self.__state), len(self.__state[0])]

    def display(self):
        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in self.__state]))
        print()
        return

    def get_neighbors(self, x, y):
        size = self.size
        r_low = x - 1 if x - 1 >= 0 else x
        r_high = x + 1 if x + 1 < size[0] else x

        c_low = y - 1 if y - 1 >= 0 else y
        c_high = y + 1 if y + 1 < size[1] else y

        return sum([int(self.__state[i][j]) for i in range(r_low, r_high + 1)
                    for j in range(c_low, c_high + 1) if i != j])

    def get_state(self):
        return self.__state.copy()

    def get_size(self):
        return self.size

    def set_state(self, state):
        if self.__state != state:
            self.__state = state
            return True
        return False


class Game:
    def __init__(self, state_file):
        self.board = Board(state_file)

    def display(self):
        self.board.display()

    def is_alive(self, v, i, j):
        neighbors = self.board.get_neighbors(i, j)
        if v == 0 and neighbors == 3:
            return 1

        if v == 1 and neighbors in [2, 3]:
            return 1

        return 0

    def get_update(self):
        state = self.board.get_state()
        r, c = self.board.get_size()

        for i in range(r):
            for j in range(c):
                state[i][j] = self.is_alive(state[i][j], i, j)
        return state

    def play(self):
        self.display()
        while True:
            new_state = self.get_update()
            did_update = self.board.set_state(new_state)
            self.display()
            if not did_update:
                break
            break
            time.sleep(1000)


def main():
    game = Game('./myfile.txt')
    game.play()


if __name__ == '__main__':
    main()
