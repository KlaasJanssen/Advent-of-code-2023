with open("data/D6.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

times = [int(x) for x in [x for x in input[0].split(" ") if not x == ""][1:]]
distances = [int(x) for x in [x for x in input[1].split(" ") if not x == ""][1:]]

score = 1
for time, distance in zip(times, distances):
    beat = 0
    for hold in range(time):
        if (time - hold) * hold > distance:
            beat += 1

    score *= beat

print(score)
