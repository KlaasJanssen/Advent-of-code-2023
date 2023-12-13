def check_differences(v1, v2):
    differences = 0
    for char1, char2 in zip(v1, v2):
        if char1 != char2:
            differences += 1

    return differences


with open("data/D13.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]
    input.append("")

score = 0
grid = []
for line in input:
    if not line == "":
        grid.append(line)
    else:
        for y in range(len(grid) - 1):
            diff = check_differences(grid[y], grid[y + 1])
            if diff <= 1:
                valid = True
                y2 = 0
                while True:
                    y2 += 1
                    if y - y2 >= 0 and y + y2 + 1 < len(grid):
                        diff += check_differences(grid[y - y2], grid[y + y2 + 1])
                        if diff > 1:
                            valid = False
                            break
                    else:
                        break

                if valid and diff == 1:
                    score += (y + 1) * 100
                    break

        if valid and diff == 1:
            grid = []
            continue

        for x in range(len(grid[0]) - 1):
            diff = check_differences([row[x] for row in grid], [row[x + 1] for row in grid])
            if diff <= 1:
                valid = True
                x2 = 0
                while True:
                    x2 += 1
                    if x - x2 >= 0 and x + x2 + 1 < len(grid[0]):
                        diff += check_differences([row[x - x2] for row in grid], [row[x + x2 + 1] for row in grid])
                        if diff > 1:
                            valid = False
                            break
                    else:
                        break

                if valid and diff == 1:
                    score += (x + 1)
                    break

        grid = []

print(score)
