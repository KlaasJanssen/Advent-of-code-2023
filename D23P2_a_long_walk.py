from collections import defaultdict

def find_connections(intersection):
    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
        start_pos = (intersection[0] + direction[0], intersection[1] + direction[1])
        if input[start_pos[1]][start_pos[0]] != "#":
            previous = intersection
            pos = (start_pos[0], start_pos[1])
            steps = 1

            path_found = False
            while not path_found:
                #print(intersection, start_pos, pos, previous)
                for direction2 in [(0,1), (0,-1), (1,0), (-1,0)]:
                    new_pos = (pos[0] + direction2[0], pos[1] + direction2[1])
                    if new_pos == previous: continue
                    if input[new_pos[1]][new_pos[0]] != "#":
                        steps += 1
                        previous = pos
                        if new_pos in intersections:
                            connections[intersection].append((new_pos, steps))
                            path_found = True
                        elif new_pos == start:
                            #connections[intersection].append(("start", steps))
                            path_found = True
                            start_connections[intersection] = steps
                            #print("check")
                        elif new_pos == end:
                            connections[intersection].append(("end", steps))
                            path_found = True
                        pos = new_pos
                        #print("check")
                        break

def find_longest_path(intersection, steps, visited):
    global max_dist
    for dest, step in connections[intersection]:
        if dest == "end":
            if steps + step > max_dist: max_dist = steps + step
            return
        if not dest in visited:
            new_visited = visited.copy()
            new_visited.append(dest)
            find_longest_path(dest, steps + step, new_visited)

with open("data/D23.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

for x, char in enumerate(input[0]):
    if char == ".":
        start = (x, 0)

for x, char in enumerate(input[-1]):
    if char == ".":
        end = (x, len(input) - 1)

intersections = []
for y, line in enumerate(input[1:-1]):
    for x, char in enumerate(line[1:-1]):
        x2 = x + 1
        y2 = y + 1

        if input[y2][x2] == "#": continue

        surrounding = 0
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            if input[y2 + direction[1]][x2 + direction[0]] != "#":
                surrounding += 1
        if surrounding >= 3:
            intersections.append((x2,y2))
            #print(x2, y2)

connections = defaultdict(list)
start_connections = defaultdict(int)

for intersection in intersections:
    find_connections(intersection)

max_dist = 0
for key, value in start_connections.items():
    find_longest_path(key, value, [key])

print(max_dist)

# for key, value in connections.items():
#     print(key, value)
