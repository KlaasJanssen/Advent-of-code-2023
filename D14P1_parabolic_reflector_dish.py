from copy import deepcopy

with open("data/D14.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

grid = []
for line in input:
    grid.append(list(line))

while True:
    grid_copy = deepcopy(grid)
    for y, row in enumerate(grid[1:]):
        for x, value in enumerate(row):
            if value == "O" and grid[y][x] == ".":
                grid[y][x] = "O"
                grid[y + 1][x] = "."

    if grid_copy == grid:
        break

score = 0
for y, row in enumerate(grid[::-1]):
    for value in row:
        if value == "O":
            score += y + 1

print(score)
