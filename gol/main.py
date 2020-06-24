import gol
import time
import curses

game = gol.GameOfLife()

print('Initial Board:')
print(game.display())
input('Start?')


def simulate(board):
    stdscr.addstr(0, 0, board)
    stdscr.refresh()


try:
    while True:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        simulate(game.display())
        try:
            game.step()
            # print(game.display())
            simulate(game.display())
            time.sleep(0.5)
        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()

except KeyboardInterrupt:
    print()
    print('Final Board')
    print(game.display())
    print(game.stats())
    exit(0)
