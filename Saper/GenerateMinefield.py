import random
def generate_maze(max_rows, max_cols, max_mines):
    if type(max_rows) is not int:
        minefield = None
    elif type(max_cols) is not int:
        minefield = None
    elif type(max_mines) is not int:
        minefield = None
    elif max_rows < 1:
        minefield = None
    elif max_cols < 1:
        minefield = None
    elif max_mines < 1:
        minefield = None
    elif max_mines > (max_rows * max_cols):
        minefield = None
    else:
        min_addr = dict()
        minefield = [[0 for col in range(max_cols)] for row in range(max_rows)]
        while(len(min_addr) < max_mines):
            min_addr[(random.randint(0, max_rows - 1), random.randint(0, max_cols - 1))] = -1
            minefield[((list(min_addr)[::-1])[0])[0]][((list(min_addr)[::-1])[0])[1]] = -1
        for a, b in min_addr:
            for c in range(max(0, a-1), min(a+2, max_rows)):
                for d in range(max(0, b-1), min(b+2, max_rows)):
                    if minefield[c][d] != -1:
                        minefield[c][d] += 1
    return minefield