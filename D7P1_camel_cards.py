from collections import defaultdict

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.hand_freq = defaultdict(int)
        for card in hand:
            self.hand_freq[card] += 1

        if 5 in self.hand_freq.values():
            self.hand_value = 7
        elif 4 in self.hand_freq.values():
            self.hand_value = 6
        elif 3 in self.hand_freq.values() and 2 in self.hand_freq.values():
            self.hand_value = 5
        elif 3 in self.hand_freq.values():
            self.hand_value = 4
        elif len([x for x in self.hand_freq.values() if x == 2]) == 2:
            self.hand_value = 3
        elif 2 in self.hand_freq.values():
            self.hand_value = 2
        else:
            self.hand_value = 1

        self.hand_order = []
        for card in self.hand:
            self.hand_order.append(order.index(card))


with open("data/D7.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

hands = []
order = "23456789TJQKA"
for line in input:
    hand, bid = line.split(" ")
    hands.append(Hand(hand, bid))

score = 0
hands_sorted = sorted(hands, key = lambda x: (x.hand_value, x.hand_order[0], x.hand_order[1], x.hand_order[2], x.hand_order[3], x.hand_order[4]))
for rank, hand in enumerate(hands_sorted):
    score += (rank + 1) * hand.bid

print(score)
