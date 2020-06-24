class Board:

    def __init__ (self x, y):
        self.x= x;
        self.y = y

        # creates an x by y board with each element initialized to 0
        Matrix = [[0 for a in range(x)] for b in range(y)]

    def display():
        for row in range(x):
            for column in range(y):
                print Matrix[row]p[column]
