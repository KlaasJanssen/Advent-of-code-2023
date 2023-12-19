with open("data/D18.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

direction = {
"3":[0,-1],
"1":[0,1],
"2":[-1,0],
"0":[1,0]
}

# direction = {
# "U":[0,-1],
# "D":[0,1],
# "L":[-1,0],
# "R":[1,0]
# }

pos = [0,0]
points = [[0,0]]
wall_length = 1
for line in input:
    hex = line.split(" ")[-1]
    num = int(hex[2:-2], 16)

    pos[0] += direction[hex[-2]][0] * num
    pos[1] += direction[hex[-2]][1] * num
    points.append(pos.copy())
    wall_length += num

#print(points)

deter_sum = 0
for index, point in enumerate(points):
    other_point = points[index - 1]
    deter_sum += other_point[0] * point[1]
    deter_sum -= other_point[1] * point[0]

print(deter_sum // 2 + wall_length // 2 + 1)
