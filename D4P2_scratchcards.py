from collections import defaultdict

with open("data/D4.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

cards_owned = defaultdict(int)

for line in input:
    card, numbers = line.split(": ")
    card = int(card.split(" ")[-1])
    cards_owned[card] += 1
    winning_numbers, my_numbers = numbers.split(" | ")
    winning_numbers = [int(x) for x in winning_numbers.split(" ") if not x == ""]
    my_numbers = [int(x) for x in my_numbers.split(" ") if not x == ""]

    hits = 0
    for number in my_numbers:
        if number in winning_numbers:
            hits += 1

    for x in range(hits):
        if card + x + 1 <= len(input):
            cards_owned[card + x + 1] += cards_owned[card]

print(sum(cards_owned.values()))
