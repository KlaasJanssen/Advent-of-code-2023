with open("data/D15.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()][0]

input = input.split(",")
score = 0

for line in input:
    value = 0
    for char in line:
        value += ord(char)
        value *= 17
        value = value % 256

    score += value

print(score)
