with open("data/D9.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    numbers = [[int(x) for x in line.split()]]
    while True:
        all_zeros = True
        for number in numbers[-1]:
            if number != 0:
                all_zeros = False
                break

        if all_zeros:
            break
        else:
            diffs = []
            for index in range(1, len(numbers[-1])):
                diffs.append(numbers[-1][index] - numbers[-1][index - 1])
            numbers.append(diffs)

    for depth in range(len(numbers) - 2, -1, -1):
        numbers[depth].append(numbers[depth][-1] + numbers[depth + 1][-1])

    score += numbers[0][-1]

print(score)
