with open("data/D6.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

time = int("".join([x for x in input[0].split(" ") if not x == ""][1:]))
distance = int("".join([x for x in input[1].split(" ") if not x == ""][1:]))

beat = 0
for hold in range(time):
    if (time - hold) * hold > distance:
        beat += 1

print(beat)
