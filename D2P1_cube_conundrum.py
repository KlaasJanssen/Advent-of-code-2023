with open("data/D2.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

max_cubes = {
    "red":12,
    "green":13,
    "blue":14
}

score = 0
for line in input:
    split_line = line.split(": ")
    draws = split_line[1].split("; ")
    valid = True
    for draw in draws:
        for color in draw.split(", "):
            split_color = color.split(" ")
            if int(split_color[0]) > max_cubes[split_color[1]]:
                valid = False
                break

    if valid:
        score += int(split_line[0].strip(":").split(" ")[-1])

print(score)
