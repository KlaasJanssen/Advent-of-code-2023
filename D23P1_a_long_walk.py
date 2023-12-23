with open("data/D23.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

for x, char in enumerate(input[0]):
    if char == ".":
        start = [x, 0]

for x, char in enumerate(input[-1]):
    if char == ".":
        end = [x, len(input) - 1]

def find_longest_path(x, y, steps_so_far, visited, previous):
    global max_dist, paths
    previous = previous.copy()

    while True:
        if [x, y] == end:
            if steps_so_far > max_dist:
                max_dist = steps_so_far
            del visited
            return

        surrounding = 0
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            if input[y + direction[1]][x + direction[0]] != "#":
                surrounding += 1
        if surrounding >= 3:
            if [x,y] in visited:
                return
            visited = visited.copy()
            visited.append([x,y])
            break

        else:
            for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if not [new_x, new_y] == previous:
                    if input[new_y][new_x] != "#":
                        if input[y][x] != ".":
                            if direction != valid_moves[input[y][x]]:
                                return
                        del previous
                        previous = [x, y]
                        steps_so_far += 1
                        x = new_x
                        y = new_y
                        break

    if input[y][x] == ">" or (input[y][x] == "." and input[y][x + 1] != "#"):
        if not [x + 1, y] == previous:
            find_longest_path(x + 1, y, steps_so_far + 1, visited, [x,y])

    if input[y][x] == "<" or (input[y][x] == "." and input[y][x - 1] != "#"):
        if not [x - 1, y] == previous:
            find_longest_path(x - 1, y, steps_so_far + 1, visited, [x,y])

    if input[y][x] == "v" or (input[y][x] == "." and input[y + 1][x] != "#"):
        if not [x, y + 1] == previous:
            find_longest_path(x, y + 1, steps_so_far + 1, visited, [x,y])

    if input[y][x] == "^" or (input[y][x] == "." and input[y - 1][x] != "#"):
        if not [x, y - 1] == previous:
            if not y - 1 == 0:
                find_longest_path(x, y - 1, steps_so_far + 1, visited, [x,y])

    #del visited_since_intersection
valid_moves = {
"<":(-1,0),
">":(1,0),
"v":(0,1),
"^":(0,-1)
}
# print(end)
# print(len(input), len(input[0]))
max_dist = 0
#print("check")
find_longest_path(start[0], 1, 1, [], start)
print(max_dist)
