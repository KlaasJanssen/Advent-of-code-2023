from collections import defaultdict

def get_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

with open("data/D15.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()][0]

input = input.split(",")
boxes = defaultdict(list)

for line in input:
    if "-" in line:
        hash = get_hash(line[:-1])
        to_remove = None
        for x in boxes[hash]:
            if x[0] == line[:-1]:
                to_remove = x
                break

        if not to_remove == None:
            boxes[hash].remove(to_remove)

    if "=" in line:
        label = line.split("=")[0]
        hash = get_hash(label)
        found = False
        for x in boxes[hash]:
            if x[0] == label:
                x[1] = int(line.split("=")[1])
                found = True
        if not found:
            boxes[hash].append([label, int(line.split("=")[1])])

score = 0
for box, lenses in boxes.items():
    for index, lens in enumerate(lenses):
        score += (box + 1) * (index + 1) * lens[1]

print(score)
