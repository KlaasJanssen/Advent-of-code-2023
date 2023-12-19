class Workflow:
    def __init__(self, conditions):
        self.conditions = []
        for condition in conditions.split(","):
            if len(condition.split(":")) == 1:
                self.conditions.append([condition])
            else:
                test, dest = condition.split(":")
                if ">" in test:
                    part, number = test.split(">")
                    self.conditions.append([part, int(number), 1, dest])
                else:
                    part, number = test.split("<")
                    self.conditions.append([part, int(number), -1, dest])

    def process_part(self, part):
        for condition in self.conditions:
            if len(condition) == 1:
                self.set_dest(part, condition[0])
                return
            else:
                if part.stats[condition[0]] * condition[2] > condition[1] * condition[2]:
                    self.set_dest(part, condition[3])
                    return

    def set_dest(self, part, dest):
        if dest == "R":
            part.accepted = False
        elif dest == "A":
            part.accepted = True
        else:
            part.workflow = dest

class Part:
    def __init__(self, stats):
        self.accepted = None
        self.workflow = "in"
        self.stats = {}
        for element in stats.split(","):
            key, value = element.split("=")
            self.stats[key] = int(value)

    def get_score(self):
        score = 0
        for num in self.stats.values():
            score += num
        return score

with open("data/D19.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

workflows = {}
building_workflows = True
score = 0
for line in input:
    if building_workflows:
        if line == "":
            building_workflows = False
        else:
            name = line[:line.index("{")]
            conditions = line[line.index("{") + 1:-1]
            workflows[name] = Workflow(conditions)

    else:
        part = Part(line[1:-1])
        while part.accepted == None:
            workflows[part.workflow].process_part(part)

        if part.accepted:
            score += part.get_score()

print(score)
