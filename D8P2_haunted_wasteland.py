with open("data/D8.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

instructions = input[0]
input = input[2:]
pos = set()

connections = {}
for line in input:
    loc, dest = line.split(" = ")
    connections[loc] = dest[1:-1].split(", ")
    if loc[-1] == "A":
        pos.add(loc)

cycles = {}
dests_reached = {}
for loc in pos:
    loc_org = loc
    steps = 0
    seen = {}
    dests_reached[loc_org] = []
    while True:
        instruction = instructions[steps % len(instructions)]
        steps += 1
        if instruction == "L":
            loc = connections[loc][0]
        else:
            loc = connections[loc][1]

        if loc in seen and not loc_org in cycles:
            if (seen[loc] - steps) % len(instructions) == 0:
                cycles[loc_org] = steps - seen[loc]
                break
        else:
            seen[loc] = steps

        if loc[-1] == "Z":
            dests_reached[loc_org].append(steps)

cycles = list(cycles.values())
change_factor = cycles[0]
score = change_factor
for cycle in cycles[1:]:
    while True:
        if score % cycle == 0:
            change_factor = score
            break
        else:
            score += change_factor

print(score)
