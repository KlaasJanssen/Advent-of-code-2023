with open("data/D3.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

current_num = ""
num_start = None

score = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char.isnumeric():
            if current_num == "":
                num_start = x
            current_num += char

        if not char.isnumeric() or x == len(line) - 1:
            if num_start != None:
                valid_part = False
                for x_check in range(num_start - 1, x + 1):
                    for y_check in range(y - 1, y + 2):
                        if x_check >= 0 and x_check < len(line) and y_check >= 0 and y_check < len(input):
                            if not input[y_check][x_check].isnumeric() and not input[y_check][x_check] == ".":
                                valid_part = True
                                break

                if valid_part:
                    score += int(current_num)

            current_num = ""
            num_start = None


print(score)
