# game-of-life
Conway's Game of Life

[description and rules](http://pi.math.cornell.edu/~lipa/mec/lesson6.html)

## Round 1

- Define a `Board` class containing cells. The board class should have a `display` method that shows the current state (all cells should be clearly alive or dead).
- Allow a board to be initialized from a .txt file that reports cell states, e.g.

```
00000100
00000100
00000100
00000000
00000000
00000000
00000000
00000000
```

defines an 8x8 board with three live cells and sixty-one dead ones.

## Round 2: Rules

- Define a main loop and a `step` function. `step` should update a board using the rules of the game of Life.
