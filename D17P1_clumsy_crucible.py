from sys import exit

class Tile:
    def __init__(self, x, y, heatloss):
        self.x = x
        self.y = y
        self.heatloss = heatloss
        self.heatloss_so_far = {}
        self.end = False
        self.visited = 0
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            for x in range(1,4):
                self.heatloss_so_far[(direction, x)] = 9000

    def open_tile(self, stats):
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
                        if in_line > 3:
                            continue
                    new_tile = grid[new_y][new_x]
                    if new_tile.end:
                        print(stats[0] + new_tile.heatloss)
                        exit()
                    if stats[0] + new_tile.heatloss < new_tile.heatloss_so_far[(direction, in_line)]:
                        new_tile.heatloss_so_far[(direction, in_line)] = stats[0] + new_tile.heatloss
                        open_tiles.append((new_x, new_y, stats[0] + new_tile.heatloss, direction, in_line))

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
open_tiles = [(0,0,0,(-1,-1),1)]

while len(open_tiles) > 0:
    #print(len(open_tiles))
    tile_stats = min(open_tiles, key = lambda x: x[2])
    tile = grid[tile_stats[1]][tile_stats[0]]
    tile.open_tile(tile_stats[2:])
    open_tiles.remove(tile_stats)
