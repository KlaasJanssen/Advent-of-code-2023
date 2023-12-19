from sys import exit

class Tile:
    def __init__(self, x, y, heatloss):
        self.x = x
        self.y = y
        self.heatloss = heatloss
        self.heatloss_so_far = {}
        self.end = False
        self.visited = 0
        self.dist_from_factory = len(input) + len(input[0]) - self.x - self.y
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            for x in range(1,11):
                self.heatloss_so_far[(direction, x)] = 2000 - self.dist_from_factory
                #self.parent[(direction, x)] = None

    def open_tile(self, stats):
        global open_tiles, path
        #rev_dir = (x * -1 for x in stats[1])
        rev_dir = (stats[1][0] * -1, stats[1][1]* -1)
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            if not direction == tuple(rev_dir):
                new_x = self.x + direction[0]
                new_y = self.y + direction[1]
                if new_x >= 0 and new_x < len(grid[0]) and new_y >= 0 and new_y < len(grid):
                    in_line = 1
                    if direction == stats[1]:
                        in_line = stats[2] + 1
                        if in_line > 10:
                            continue
                    if direction != stats[1] and stats[2] < 4:
                        continue
                    new_tile = grid[new_y][new_x]
                    if new_tile.end:
                        if stats[2] < 4 or direction != stats[1]:
                            continue
                        #print(direction, stats[1])
                        #new_tile.parent[(direction, in_line)] = (self.x, self.y, *stats)
                        print(stats[0] + new_tile.heatloss)
                        # print(stats)
                        #path = []
                        open_tiles = [(self.x, self.y, stats[0], stats[1], stats[2])]
                        #new_tile.get_path(new_tile.parent[(direction, in_line)])
                        return
                    if stats[0] + new_tile.heatloss < new_tile.heatloss_so_far[(direction, in_line)]:
                        new_tile.heatloss_so_far[(direction, in_line)] = stats[0] + new_tile.heatloss
                        #new_tile.parent[(direction, in_line)] = (self.x, self.y, *stats)
                        open_tiles.append((new_x, new_y, stats[0] + new_tile.heatloss, direction, in_line))

    def get_path(self, parent):
        global path, total_heatloss
        if parent[0] == 0 and parent[1] == 0:
            return
        else:
            total_heatloss += self.heatloss
            path.append((self.x, self.y))
            tile = grid[parent[1]][parent[0]]
            tile.get_path(tile.parent[(parent[3], parent[4])])

total_heatloss = 0
with open("data/D17.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

grid = []
for y, line in enumerate(input):
    row = []
    for x, num in enumerate(line):
        row.append(Tile(x, y, int(num)))
    grid.append(row)

grid[-1][-1].end = True
open_tiles = [(0,0,0,(0,1),0), (0,0,0,(1,0),0)]

while len(open_tiles) > 0:
    #print(len(open_tiles))
    #print(open_tiles)
    tile_stats = min(open_tiles, key = lambda x: x[2])
    tile = grid[tile_stats[1]][tile_stats[0]]
    tile.open_tile(tile_stats[2:])
    open_tiles.remove(tile_stats)

# show_grid = [list("."*len(input[0])) for x in range(len(input))]
# for tile in path:
#     show_grid[tile[1]][tile[0]] = "#"
#
# for row in show_grid:
#     print("".join(row))
