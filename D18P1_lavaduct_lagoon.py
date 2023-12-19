with open("data/D18.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

direction = {
"U":[0,-1],
"D":[0,1],
"L":[-1,0],
"R":[1,0]
}

pos = [0,0]
walls = [[0,0]]
for line in input:
    split_line = line.split(" ")[:-1]
    for x in range(1, int(split_line[1]) + 1):
        pos[0] += direction[split_line[0]][0]
        pos[1] += direction[split_line[0]][1]
        walls.append(pos.copy())

min_x = min(walls, key = lambda x: x[0])[0]
max_x = max(walls, key = lambda x: x[0])[0]
min_y = min(walls, key = lambda x: x[1])[1]
max_y = max(walls, key = lambda x: x[1])[1]
print(min_x, max_x, min_y, max_y)

outside = [[min_x - 1, min_y - 1]]
open_tiles = [outside[0].copy()]

while len(open_tiles) > 0:
    new_open_tiles = []
    for tile in open_tiles:
        for direction in [[0,1], [0,-1], [1,0], [-1,0]]:
            new_pos = tile.copy()
            new_pos[0] += direction[0]
            new_pos[1] += direction[1]
            #print(new_pos)
            if new_pos[0] >= min_x - 1 and new_pos[0] <= max_x + 1 and new_pos[1] >= min_y - 1 and new_pos[1] <= max_y + 1:
                #print("check")
                if not new_pos in walls and not new_pos in outside:
                    outside.append(new_pos)
                    new_open_tiles.append(new_pos)

    open_tiles = new_open_tiles
    print(len(outside))

#print((max_x - min_x + 3) * (max_y - min_y + 3))
print((max_x - min_x + 3) * (max_y - min_y + 3) - len(outside))
