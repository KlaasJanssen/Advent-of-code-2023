with open("data/D8.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

instructions = input[0]
input = input[2:]

connections = {}
for line in input:
    loc, dest = line.split(" = ")
    connections[loc] = dest[1:-1].split(", ")

steps = 0
pos = "AAA"
while True:
    instruction = instructions[steps % len(instructions)]
    steps += 1
    if instruction == "L":
        pos = connections[pos][0]
    else:
        pos = connections[pos][1]

    if pos == "ZZZ":
        print(steps)
        break
