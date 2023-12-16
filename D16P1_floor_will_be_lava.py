with open("data/D16.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

energized = set()
visited = set()
lasers = [(-1,0,0)]

direction = {
0:[1,0],
1:[0,1],
2:[-1,0],
3:[0,-1]
}

while len(lasers) > 0:
    new_lasers = []
    for laser in lasers:
        new_pos = (laser[0] + direction[laser[2]][0], laser[1] + direction[laser[2]][1])
        if new_pos[0] >= 0 and new_pos[0] < len(input[0]) and new_pos[1] >= 0 and new_pos[1] < len(input):
            energized.add(new_pos)
            match input[new_pos[1]][new_pos[0]]:
                case ".":
                    if not (new_pos[0], new_pos[1], laser[2]) in visited:
                        visited.add((new_pos[0], new_pos[1], laser[2]))
                        new_lasers.append((new_pos[0], new_pos[1], laser[2]))
                case "\\":
                    if laser[2] in [0, 2]:
                        new_direction = (laser[2] + 1) % 4
                    else:
                        new_direction = (laser[2] - 1) % 4
                    if not (new_pos[0], new_pos[1], new_direction) in visited:
                        visited.add((new_pos[0], new_pos[1], new_direction))
                        new_lasers.append((new_pos[0], new_pos[1], new_direction))
                case "/":
                    if laser[2] in [0, 2]:
                        new_direction = (laser[2] - 1) % 4
                    else:
                        new_direction = (laser[2] + 1) % 4
                    if not (new_pos[0], new_pos[1], new_direction) in visited:
                        visited.add((new_pos[0], new_pos[1], new_direction))
                        new_lasers.append((new_pos[0], new_pos[1], new_direction))
                case "-":
                    if laser[2] in [0, 2]:
                        if not (new_pos[0], new_pos[1], laser[2]) in visited:
                            visited.add((new_pos[0], new_pos[1], laser[2]))
                            new_lasers.append((new_pos[0], new_pos[1], laser[2]))
                    else:
                        if not (new_pos[0], new_pos[1], 0) in visited:
                            visited.add((new_pos[0], new_pos[1], 0))
                            new_lasers.append((new_pos[0], new_pos[1], 0))
                        if not (new_pos[0], new_pos[1], 2) in visited:
                            visited.add((new_pos[0], new_pos[1], 2))
                            new_lasers.append((new_pos[0], new_pos[1], 2))
                case "|":
                    if laser[2] in [1, 3]:
                        if not (new_pos[0], new_pos[1], laser[2]) in visited:
                            visited.add((new_pos[0], new_pos[1], laser[2]))
                            new_lasers.append((new_pos[0], new_pos[1], laser[2]))
                    else:
                        if not (new_pos[0], new_pos[1], 1) in visited:
                            visited.add((new_pos[0], new_pos[1], 1))
                            new_lasers.append((new_pos[0], new_pos[1], 1))
                        if not (new_pos[0], new_pos[1], 3) in visited:
                            visited.add((new_pos[0], new_pos[1], 3))
                            new_lasers.append((new_pos[0], new_pos[1], 3))

    lasers = new_lasers
    #print(lasers)

print(len(energized))
#print(energized)
