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
visited = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            open_pos.append([x, y])
            visited.append([x, y])

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
                if not new_pos in visited:
                    reverse_direction = [x*-1 for x in direction]
                    if reverse_direction in directions[input[new_pos[1]][new_pos[0]]]:
                        new_open_pos.append(new_pos)
                        visited.append(new_pos)

    #print(new_open_pos)
    open_pos = new_open_pos

print(steps - 1)
