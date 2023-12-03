with open("data/D1.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    first = True
    first_num, last_num = None, None

    for char in line:
        if char.isnumeric():
            if first:
                first_num = char
                first = False
            last_num = char

    score += int(first_num + last_num)

print(score)
