
class Board:
    board = []

    # initializes board using a text file
    def __init__(board.txt):
        file = open txt file 
        for i in range[0,7]
            col = []
            for j in range[0,7]
                cols.append(file.nextCharacter)
            this.board.append(col)

    # display board's current state
    def display():
        for row in this.board:
            for col in this.board:
                print(col)
            print('\n')

    def step():
        # iterate through this.board in row major order
        for row in this.board:
            for col in this.board:
                state = this.board[row - 1][col - 1] + this.board[row - 1][col] + this.board[row - 1][col + 1]
                 + this.board[row][col - 1] + this.board[row][col + 1] + this.board[row + 1][col - 1] 
                 + this.board[row + 1][col] + this.board[row + 1][col + 1]

                # TODO need to consider border/ edge cases

                if col == True: # alive
                    # check if it has either 2 or 3 live neighbours
                    if (state == 2 | state == 3)
                        pass
                    else 
                        col = 0
                else: # dead
                    # check if it has 3 live neighbours
                    if (state == 3)
                        col = 1

    def main():
        while True: 
            step()

    if __name__ == '__main__'
        main()
