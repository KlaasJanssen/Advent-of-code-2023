def get_all_configurations(spots):
    configurations = [""]
    for index, char in enumerate(spots):
        new_configurations = []
        for configuration in configurations:
            if char in [".", "?"]:
                new_configurations.append(configuration + ".")
            if char in ["#", "?"]:
                new_configurations.append(configuration + "#")
        configurations = new_configurations

    return configurations

def check_configuration(spots, damaged):
    spots += "."
    current_damaged = 0
    for char in spots:
        if char == "." and current_damaged > 0:
            if current_damaged == damaged[0]:
                damaged.pop(0)
                current_damaged = 0
            else:
                return False
        if char == "#":
            if len(damaged) == 0:
                return False
            else:
                current_damaged += 1

    if len(damaged) == 0:
        return True
    else:
        return False

with open("data/D12.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

score = 0
for line in input:
    #print(score)
    springs, damaged = line.split(" ")
    damaged = [int(x) for x in damaged.split(",")]
    spots = [x for x in springs.split(".") if not x == ""]
    all_configurations = get_all_configurations(".".join(spots))

    for configuration in all_configurations:
        if check_configuration(configuration, damaged.copy()):
            #print(configuration)
            score += 1


print(score)
