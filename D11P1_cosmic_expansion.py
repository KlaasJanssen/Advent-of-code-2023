with open("data/D11.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

galaxies = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append([x, y])

all_x = set([x[0] for x in galaxies])
all_y = set([x[1] for x in galaxies])

for x in range(max(all_x))[::-1]:
    if not x in all_x:
        for galaxy in galaxies:
            if galaxy[0] > x:
                galaxy[0] += 1

for y in range(max(all_y))[::-1]:
    if not y in all_y:
        for galaxy in galaxies:
            if galaxy[1] > y:
                galaxy[1] += 1

score = 0
for index, galaxy1 in enumerate(galaxies[:-1]):
    for galaxy2 in galaxies[index+1:]:
        score += abs(galaxy1[0] - galaxy2[0])
        score += abs(galaxy1[1] - galaxy2[1])

print(score)
