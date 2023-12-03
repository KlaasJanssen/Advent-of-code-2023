with open("data/D3.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

current_num = ""
num_start = None

gears = {}

score = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char.isnumeric():
            if current_num == "":
                num_start = x
            current_num += char

        if not char.isnumeric() or x == len(line) - 1:
            if num_start != None:
                for x_check in range(num_start - 1, x + 1):
                    for y_check in range(y - 1, y + 2):
                        if x_check >= 0 and x_check < len(line) and y_check >= 0 and y_check < len(input):
                            if input[y_check][x_check] == "*":
                                if str((x_check, y_check)) in gears.keys():
                                    gears[str((x_check, y_check))] = (gears[str((x_check, y_check))][0] * int(current_num), gears[str((x_check, y_check))][1] + 1)
                                else:
                                    gears[str((x_check, y_check))] = (int(current_num), 1)

            current_num = ""
            num_start = None

score = 0
for gear in gears.values():
    if gear[1] == 2:
        score += gear[0]

print(score)
