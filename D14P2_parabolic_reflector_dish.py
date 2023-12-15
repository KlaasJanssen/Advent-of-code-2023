from copy import deepcopy

with open("data/D14.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

cycles = []
grid = []
for line in input:
    grid.append(list(line))

iter = 0
cycle_found = False
while iter < 1e9:
    while True:
        grid_copy = deepcopy(grid)
        for y, row in enumerate(grid[1:]):
            for x, value in enumerate(row):
                if value == "O" and grid[y][x] == ".":
                    grid[y][x] = "O"
                    grid[y + 1][x] = "."

        if grid_copy == grid:
            break

    while True:
        grid_copy = deepcopy(grid)
        for y, row in enumerate(grid):
            for x, value in enumerate(row[1:]):
                if value == "O" and grid[y][x] == ".":
                    grid[y][x] = "O"
                    grid[y][x + 1] = "."

        if grid_copy == grid:
            break

    while True:
        grid_copy = deepcopy(grid)
        for y, row in enumerate(grid[:-1]):
            for x, value in enumerate(row):
                if value == "O" and grid[y + 1][x] == ".":
                    grid[y + 1][x] = "O"
                    grid[y][x] = "."

        if grid_copy == grid:
            break

    while True:
        grid_copy = deepcopy(grid)
        for y, row in enumerate(grid):
            for x, value in enumerate(row[:-1]):
                if value == "O" and grid[y][x + 1] == ".":
                    grid[y][x + 1] = "O"
                    grid[y][x] = "."

        if grid_copy == grid:
            break

    if not cycle_found:
        grid_str = "".join(["".join(x) for x in grid])
        if grid_str in cycles:
            cycle_found = True
            cycle_length = iter - cycles.index(grid_str)
            cycles_to_add = (1e9 - iter) // cycle_length
            iter += cycles_to_add * cycle_length
            #break
        cycles.append(grid_str)
    iter += 1

# for row in grid:
#     print("".join(row))

score = 0
for y, row in enumerate(grid[::-1]):
    for value in row:
        if value == "O":
            score += y + 1

print(score)
