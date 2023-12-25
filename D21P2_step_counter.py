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

x1 = 0
x2 = 0
pos_pos = set()
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            pos_pos.add((x,y))
            input[y] = input[y][:x] + "." + input[y][x+1:]
        if char in [".", "S"]:
            if (x + y) % 2 == 0:
                if char == "S":
                    print("x1")
                x1 += 1
            else:
                if char == "S":
                    print("x2")
                x2 += 1

for x in range(140):
    new_pos_pos = set()
    for pos in pos_pos:
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = pos[0] + direction[0]
            new_y = pos[1] + direction[1]
            if new_x >= 0 and new_x < len(input[0]) and new_y >= 0 and new_y < len(input):
                if input[new_y][new_x] != "#":
                    new_pos_pos.add((new_x, new_y))
    pos_pos = new_pos_pos
    if x == 64:
        x1_diamond = len(pos_pos)

#print_grid(input)

x1 = len(pos_pos)

new_pos_pos = set()
for pos in pos_pos:
    for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_x = pos[0] + direction[0]
        new_y = pos[1] + direction[1]
        if new_x >= 0 and new_x < len(input[0]) and new_y >= 0 and new_y < len(input):
            if input[new_y][new_x] != "#":
                new_pos_pos.add((new_x, new_y))
pos_pos = new_pos_pos
x2 = len(pos_pos)

pos_pos = set()
pos_pos.add((0,0))
pos_pos.add((0,130))
pos_pos.add((130,0))
pos_pos.add((130,130))

for x in range(64):
    new_pos_pos = set()
    for pos in pos_pos:
        for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x = pos[0] + direction[0]
            new_y = pos[1] + direction[1]
            if new_x >= 0 and new_x < len(input[0]) and new_y >= 0 and new_y < len(input):
                if input[new_y][new_x] != "#":
                    new_pos_pos.add((new_x, new_y))
    pos_pos = new_pos_pos


#print_grid(input)
x2_diamond = len(pos_pos)

state1 = 0
state2 = 0
state3 = 0
state4 = 0
n = (26501365 - 65) // 131
#n = 2

for x in range(1,n + 1):
    if x == 1:
        state1 += 1
    else:
        if x % 2 == 0:
            state2 += 4*x - 4
        else:
            state1 += 4*x - 4

total1 = x1 * (n - 1) * 3 + 74 * (n-1) + x1_diamond * (n-1) - 65 * (n-1) * 4
total2 = state1 * x2 + state2 * x1
total3 = x2_diamond * n
total4 = 2 * x1 + 2 * x1_diamond - 32*4 + 4

print(total1)
print(total2)
print(total3)
print(total4)
print(total1 + total2 + total3 + total4)
