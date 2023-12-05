with open("data/D5.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]
    input.append("")

seeds = [int(x) for x in input[0].split(": ")[-1].split(" ")]
input = input[3:]

new_seeds = []
for line in input:
    if line == "":
        for seed in seeds:
            new_seeds.append(seed)
        seeds = new_seeds
        new_seeds = []
    elif line[-1] == ":":
        continue

    else:
        numbers = [int(x) for x in line.split(" ")]
        for seed in seeds[::-1]:
            if seed >= numbers[1] and seed < numbers[1] + numbers[2]:
                offset = seed - numbers[1]
                new_seeds.append(numbers[0] + offset)
                seeds.remove(seed)

print(min(seeds))
