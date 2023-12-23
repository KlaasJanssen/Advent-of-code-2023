class Brick:
    def __init__(self, ID, start, end):
        self.ID = ID
        self.start = start
        self.end = end
        self.blocks = []
        self.size = [x2 - x1 + 1 for x1, x2 in zip(self.start, self.end)]
        #print(self.size)
        if self.start[2] - self.end[2] != 0:
            self.orientation = "vertical"
            # if self.start[1] - self.end[1] != 0 or self.start[0] - self.end[0] != 0:
            #     print("square_block")
        else:
            self.orientation = "horizontal"

        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                for z in range(self.start[2], self.end[2] + 1):
                    self.blocks.append([x, y, z])

        self.supports = set()
        self.supported_by = set()

        #print(len(self.blocks))

with open("data/D22.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

bricks = []
#bricks_dict = {}
for ID, line in enumerate(input):
    start, end = line.split("~")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    brick = Brick(ID, start, end)
    bricks.append(brick)
    #bricks_dict[ID] = brick

bricks = sorted(bricks, key = lambda x: x.start[2])

max_x = max(bricks, key = lambda x: x.end[0]).end[0]
max_y = max(bricks, key = lambda x: x.end[1]).end[1]

grid = []
for y in range(max_x + 1):
    row = []
    for x in range(max_y + 1):
        row.append((0, "ground"))
    grid.append(row)

for brick in bricks:
    if brick.orientation == "vertical":
        old_height = grid[brick.end[1]][brick.end[0]]
        if not old_height[1] == "ground":
            brick.supported_by.add(old_height[1])
            old_height[1].supports.add(brick)
        grid[brick.end[1]][brick.end[0]] = (old_height[0] + brick.size[2], brick)
    else:
        max_height = 0
        max_height_tiles = []
        for block in brick.blocks:
            if grid[block[1]][block[0]][0] >= max_height:
                if max_height == grid[block[1]][block[0]][0]:
                    if max_height != 0:
                        max_height_tiles.append(grid[block[1]][block[0]][1])
                else:
                    max_height = grid[block[1]][block[0]][0]
                    max_height_tiles = [grid[block[1]][block[0]][1]]
        #print(brick.ID, max_height_tiles)

        for tile in max_height_tiles:
            brick.supported_by.add(tile)
            tile.supports.add(brick)

        for block in brick.blocks:
            grid[block[1]][block[0]] = (max_height + 1, brick)

score = 0
for brick in bricks:
    can_be_destroyed = True
    for brick2 in brick.supports:
        if len(brick2.supported_by) == 1:
            can_be_destroyed = False
            break

    if can_be_destroyed:
        score += 1

print(score)
    #print([x.ID for x in brick.supports], [x.ID for x in brick.supported_by])
