with open("data/D2.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    split_line = line.split(": ")
    draws = split_line[1].split("; ")
    current_cubes = {
        "red":0,
        "green":0,
        "blue":0
    }

    for draw in draws:
        for color in draw.split(", "):
            split_color = color.split(" ")
            if int(split_color[0]) > current_cubes[split_color[1]]:
                current_cubes[split_color[1]] = int(split_color[0])

    score += current_cubes["red"] * current_cubes["green"] * current_cubes["blue"]

print(score)
