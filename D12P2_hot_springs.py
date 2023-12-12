from functools import cache

with open("data/D12.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

@cache
def get_all_combinations(spring, damaged, num_damaged):
    if len(spring) == 0:
        if (len(damaged) == 0 and num_damaged == 0) or (damaged[0] == num_damaged and len(damaged) == 1):
            return 1
        else:
            return 0

    combinations = 0
    if spring[0] in ["#", "?"]:
        combinations += get_all_combinations(spring[1:], damaged, num_damaged + 1)

    if spring[0] in [".", "?"]:
        if num_damaged > 0 and len(damaged) > 0:
            if num_damaged == damaged[0]:
                combinations += get_all_combinations(spring[1:], damaged[1:], 0)
        elif num_damaged > 0 and len(damaged) == 0:
            pass
        else:
            combinations += get_all_combinations(spring[1:], damaged, 0)

    return combinations

score = 0
for line in input:
    spring, damaged = line.split(" ")
    damaged = tuple(int(x) for x in damaged.split(","))
    #score += get_all_combinations(spring + ".", damaged, 0)
    score += get_all_combinations("?".join([spring]*5) + ".", damaged*5, 0)

print(score)
