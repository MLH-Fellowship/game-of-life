class Board:
    """Grid of two-state cells."""

    def __init__(self, state_file=None):
        """Initializes board with cell states from state_file.

        Args:
            state_file: file containing bit strings corresponding to cell states
        """
        self._cells = set()
        max_length = 0
        num_rows = 0
        with open(state_file, 'r') as inp:
            for i, line in enumerate(inp):
                # Strips out crufty bits.

                line = ''.join([bit for bit in line if bit in '01'])
                if not line:
                    continue

                # Keeps board size tidy.
                num_rows += 1
                max_length = max([max_length, len(line)])

                for j, bit in enumerate(line):
                    if bit == '1':
                        self._cells.add((i, j))

        # Creates a square board.
        self._side_length = max([max_length, num_rows])
        assert self._side_length > 4, \
            f"A board with side_length {side_length} is not interesting."

    def display(self):
        rows = []
        for i in range(self._side_length):
            row = []
            for j in range(self._side_length):
                row.append('1' if (i, j) in self._cells else '0')
            rows.append(row)
        for row in rows:
            print(''.join(row))

    def _live_neighbors(self, i, j):
        return sum(
            (_i, _j) in self._cells
            for _i in range(i - 1, i + 2)
            for _j in range(j - 1, j + 2))

    def _should_live(self, i, j):
        if (i, j) in self._cells:
            return self._live_neighbors(i, j) in {2, 3}
        else:
            return self._live_neighbors(i, j) == 3

    def update(self):
        live_cells = set()
        for i, j in self._cells:
            for _i in range(i - 1, i + 2):
                for _j in range(j - 1, j + 2):
                    if self._should_live(_i, _j):
                        live_cells.add((_i, _j))
        self._cells = live_cells
