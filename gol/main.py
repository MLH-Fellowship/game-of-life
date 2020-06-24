import gol
import time
game = gol.GameOfLife()

print('Initial Board:')
print(game.display())

while True:
    try:
        game.step()
        print(game.display())
        time.sleep(0.5)
    except KeyboardInterrupt:
        print()
        print('Final Board')
        print(game.display())
        exit(0)
