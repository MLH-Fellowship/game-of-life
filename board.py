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
                max_length = max([max_length, len(lines)])

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
