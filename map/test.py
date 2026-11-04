grid = [
            [5, 5, 5, 5, 5, 5],
            [5, 0, 2, 0, 0, 5],
            [5, 0, 0, 0, 0, 5],
            [1, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5],
            ]

def show_map():
    for i in range(len(grid)):
        for j in grid[i]:
            if (j == 5):
                print("==", end="")
            elif (j == 0):
                print("x", end="")
            elif (j == 2):
                print("O", end="")
            else:
                print(f"{j} ",end="")
        print()

show_map()