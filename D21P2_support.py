import sys

def print_grid(input):
    for index in range(len(input)):
        input[index] = list(input[index])

    for pos in pos_pos:
        input[pos[1]][pos[0]] = "O"

    for line in input:
        print("".join(line))
    sys.exit()

with open("data/D21.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

for index in range(len(input)):
    input[index] *= 5

new_input = input.copy()
for x in range(4):
    for line in input:
        new_input.append(line)
input = new_input

x1 = 0
x2 = 0

pos_pos = set()
pos_pos.add((len(input) // 2, len(input) // 2))
#print(pos_pos)
# for line in input:
#     print(line)
# pos_pos.add((0,0))
# pos_pos.add((0,130))
# pos_pos.add((130,0))
# pos_pos.add((130,130))

for x in range(65 + 131 + 131):
    new_pos_pos = set()
    for pos in pos_pos:
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = pos[0] + direction[0]
            new_y = pos[1] + direction[1]
            if new_x >= 0 and new_x < len(input[0]) and new_y >= 0 and new_y < len(input):
                if input[new_y][new_x] != "#":
                    new_pos_pos.add((new_x, new_y))
    pos_pos = new_pos_pos

test_len = len(pos_pos)
#print(test_len)
total1 = 0
total2 = 0
total3 = 0
total4 = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        #print(abs(x // 131 - 2))
        if abs(x // 131 - 2) + abs(y // 131 - 2) == 2 and x // 131 != 2 and y // 131 != 2:
            if (x, y) in pos_pos:
                total1 += 1

        if abs(x // 131 - 2) + abs(y // 131 - 2) < 2:
            if (x, y) in pos_pos:
                total2 += 1

        if abs(x // 131 - 2) + abs(y // 131 - 2) == 3:
            if (x, y) in pos_pos:
                total3 += 1

        if abs(x // 131 - 2) + abs(y // 131 - 2) == 2 and (x // 131 == 2 or y // 131 == 2):
            if (x, y) in pos_pos:
                total4 += 1

print(total1)
print(total2)
print(total3)
print(total4)
print(total1 + total2 + total3 + total4)
