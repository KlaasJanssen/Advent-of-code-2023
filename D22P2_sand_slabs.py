class Brick:
    def __init__(self, ID, start, end):
        self.ID = ID
        self.start = start
        self.end = end
        self.blocks = []
        self.size = [x2 - x1 + 1 for x1, x2 in zip(self.start, self.end)]
        if self.start[2] - self.end[2] != 0:
            self.orientation = "vertical"
        else:
            self.orientation = "horizontal"

        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                for z in range(self.start[2], self.end[2] + 1):
                    self.blocks.append([x, y, z])

        self.supports = set()
        self.supported_by = set()

with open("data/D22.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

bricks = []
for ID, line in enumerate(input):
    start, end = line.split("~")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    brick = Brick(ID, start, end)
    bricks.append(brick)

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
        else:
            brick.supported_by.add("ground")
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

        for tile in max_height_tiles:
            brick.supported_by.add(tile)
            tile.supports.add(brick)

        if len(max_height_tiles) == 0:
            brick.supported_by.add("ground")

        for block in brick.blocks:
            grid[block[1]][block[0]] = (max_height + 1, brick)

score = 0
lets_fall = {}
for brick in bricks[::-1]:
    falling_bricks = set()
    falling_bricks.add(brick)
    while True:
        new_falling_bricks = falling_bricks.copy()
        for brick2 in bricks:
            if not brick2 in new_falling_bricks:
                falling = True
                for support_brick in brick2.supported_by:
                    if support_brick == "ground":
                        falling = False
                        break
                    else:
                        if not support_brick in falling_bricks:
                            falling = False
                            break

                if falling:
                    new_falling_bricks.add(brick2)
                    if brick2.ID in lets_fall:
                        for brick3 in lets_fall[brick2.ID]:
                            new_falling_bricks.add(brick3)

        if falling_bricks == new_falling_bricks:
            break

        falling_bricks = new_falling_bricks
    score += len(falling_bricks) - 1
    lets_fall[brick.ID] = falling_bricks
print(score)
