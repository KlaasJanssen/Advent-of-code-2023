with open("data/D1.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    first = True
    first_num, last_num = None, None
    
    for index, char in enumerate(line):
        spelled_number = None
        for number, spelled in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[index:].startswith(spelled):
                spelled_number = str(number + 1)
                if first:
                    first_num = spelled_number
                    first = False
                last_num = spelled_number

        if char.isnumeric():
            if first:
                first_num = char
                first = False
            last_num = char

    score += int(first_num + last_num)

print(score)
