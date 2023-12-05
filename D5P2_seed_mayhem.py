def combine_ranges(seeds):
    new_seeds = []
    for seed1 in seeds:
        overlap = False
        for seed2 in new_seeds:
            if (seed1[0] <= seed2[1] and seed1[1] >= seed2[0]):
                seed2[0] = min(seed1[0], seed2[0])
                seed2[1] = max(seed1[1], seed2[1])
                overlap = True
        if not overlap:
            new_seeds.append(seed1)

    return new_seeds

with open("data/D5.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]
    input.append("")

temp = [int(x) for x in input[0].split(": ")[-1].split(" ")]
seeds = []
for index in range(0, len(temp), 2):
    seeds.append([temp[index], temp[index] + temp[index + 1] - 1])
input = input[3:]

new_seeds = []
for line in input:
    if line == "":
        for seed in seeds:
            new_seeds.append(seed)
        seeds = combine_ranges(new_seeds)
        new_seeds = []

    elif line[-1] == ":":
        continue

    else:
        numbers = [int(x) for x in line.split(" ")]
        not_affected = []
        while len(seeds) > 0:
            seed = seeds.pop()
            if seed[0] >= numbers[1] and seed[1] < numbers[1] + numbers[2]:
                new_seed = seed.copy()
                new_seed[0] = numbers[0] + seed[0] - numbers[1]
                new_seed[1] = numbers[0] + seed[1] - numbers[1]
                new_seeds.append(new_seed)

            elif seed[0] < numbers[1] and seed[1] >= numbers[1] and seed[1] < numbers[1] + numbers[2]:
                not_affected.append([seed[0], numbers[1]-1])
                new_seeds.append([numbers[0], numbers[0] + seed[1] - numbers[1]])

            elif seed[0] >= numbers[1] and seed[0] < numbers[1] + numbers[2] and seed[1] >= numbers[1] + numbers[2]:
                not_affected.append([numbers[1] + numbers[2], seed[1]])
                new_seeds.append([numbers[0] + seed[0] - numbers[1], numbers[0] + numbers[2] - 1])


            elif seed[0] < numbers[1] and seed[1] >= numbers[1] + numbers[2]:
                not_affected.append([seed[0], numbers[1]-1])
                not_affected.append([numbers[1] + numbers[2], seed[1]])
                new_seeds.append([numbers[0], numbers[0] + numbers[2] - 1])

            else:
                not_affected.append(seed)

        seeds = not_affected

print(min(seeds, key = lambda x: x[0])[0])
