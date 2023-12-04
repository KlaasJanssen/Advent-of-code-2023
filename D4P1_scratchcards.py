with open("data/D4.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    card, numbers = line.split(": ")
    winning_numbers, my_numbers = numbers.split(" | ")
    winning_numbers = [int(x) for x in winning_numbers.split(" ") if not x == ""]
    my_numbers = [int(x) for x in my_numbers.split(" ") if not x == ""]

    hits = 0
    for number in my_numbers:
        if number in winning_numbers:
            hits += 1

    score += 2**(hits - 1) if hits > 0 else 0

print(score)
