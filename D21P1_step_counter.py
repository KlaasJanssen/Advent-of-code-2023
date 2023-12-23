with open("data/D21.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

pos_pos = set()
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            pos_pos.add((x,y))

#print(pos_pos)

for x in range(64):
    new_pos_pos = set()
    for pos in pos_pos:
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = pos[0] + direction[0]
            new_y = pos[1] + direction[1]
            if new_x >= 0 and new_x < len(input[0]) and new_y >= 0 and new_y < len(input):
                if input[new_y][new_x] != "#":
                    new_pos_pos.add((new_x, new_y))

    pos_pos = new_pos_pos

print(len(pos_pos))
