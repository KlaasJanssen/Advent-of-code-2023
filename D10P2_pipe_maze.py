with open("data/D10.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

directions = {
"|":[[0,1], [0,-1]],
"-":[[1,0], [-1,0]],
"L":[[0,-1], [1,0]],
"J":[[0,-1], [-1,0]],
"7":[[-1,0], [0,1]],
"F":[[0,1], [1,0]],
"S":[[0,1], [0,-1], [1,0], [-1,0]],
".":[]
}

open_pos = []
in_loop = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            open_pos.append([x, y])
            in_loop.append([x, y])

steps = 0
while len(open_pos) > 0:
    steps += 1
    new_open_pos = []
    for pos in open_pos:
        for direction in directions[input[pos[1]][pos[0]]]:
            new_pos = pos.copy()
            new_pos[0] += direction[0]
            new_pos[1] += direction[1]
            if new_pos[0] >= 0 and new_pos[0] < len(input[0]) and new_pos[1] >= 0 and new_pos[1] < len(input):
                if not new_pos in in_loop:
                    reverse_direction = [x*-1 for x in direction]
                    if reverse_direction in directions[input[new_pos[1]][new_pos[0]]]:
                        new_open_pos.append(new_pos)
                        in_loop.append(new_pos)

    #print(new_open_pos)
    open_pos = new_open_pos

open_pos = []
outside = []
for x in range(len(input[0])):
    if not [x, 0] in in_loop:
        open_pos.append([x, 0])
        outside.append([x, 0])
    if not [x, len(input) - 1] in in_loop:
        open_pos.append([x, len(input) - 1])
        outside.append([x, len(input) - 1])

for y in range(1, len(input) - 1):
    if not [0, y] in in_loop:
        open_pos.append([0, y])
        outside.append([0, y])
    if not [len(input[0]) - 1, y] in in_loop:
        open_pos.append([len(input[0]) - 1, y])
        outside.append([len(input[0]) - 1, y])

while len(open_pos) > 0:
    new_open_pos = []
    for pos in open_pos:
        for direction in directions["S"]:
            new_pos = pos.copy()
            new_pos[0] += direction[0]
            new_pos[1] += direction[1]
            if new_pos[0] >= 0 and new_pos[0] < len(input[0]) and new_pos[1] >= 0 and new_pos[1] < len(input):
                if not new_pos in outside and not new_pos in in_loop:
                    new_open_pos.append(new_pos)
                    outside.append(new_pos)

    open_pos = new_open_pos
    #print(len(open_pos))

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if not [x,y] in in_loop and not [x,y] in outside:
            passed = 0
            opened = None
            for x_check in range(x)[::-1]:
                if [x_check, y] in outside:
                    break
                if [x_check, y] in in_loop:
                    match input[y][x_check]:
                        case "|":
                            passed += 1
                            opened = None
                        case "L":
                            if opened == "J":
                                passed -= 0.5
                                opened = None
                            else:
                                passed += 0.5

                        case "J":
                            passed += 0.5
                            opened = "J"
                        case "7":
                            passed += 0.5
                            opened = "7"
                        case "S":
                            passed += 0.5
                            opened = "7"
                        case "F":
                            if opened == "7":
                                opened = None
                                passed -= 0.5
                            else:
                                passed += 0.5

            if passed % 2 == 0:
                #print([x,y])
                outside.append([x,y])

print(len(in_loop))
print(len(outside))
print(len(input[0]) * len(input) - len(in_loop) - len(outside))
