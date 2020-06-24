import numpy as np
import matplotlib.pyplot as plt

class Board:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros(rows*cols).reshape((rows,cols))

    def display(self):
    	for row in self.grid:
		    for val in row:
		        print(val, end =" ")  
		    print()

	def read(self):
		with open('demo.txt') as f:
            grid = f.readlines()
        for r in grid:
            self.board.append([c for c in r.strip()])
 


