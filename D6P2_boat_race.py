import math

with open("data/D6.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

time = int("".join([x for x in input[0].split(" ") if not x == ""][1:]))
distance = int("".join([x for x in input[1].split(" ") if not x == ""][1:]))

# c = distance
# b = time
# x = time holding the button
# c = (b - x) * x
# c = bx - x**2
# x**2 - bx + c = 0

t1 = int((time + math.sqrt(time**2 - 4*distance)) / 2)
t2 = int((time - math.sqrt(time**2 - 4*distance)) / 2)

print(abs(t2 - t1))
