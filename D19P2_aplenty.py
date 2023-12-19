from copy import deepcopy

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
                    self.conditions.append([part, int(number), ">", dest])
                else:
                    part, number = test.split("<")
                    self.conditions.append([part, int(number), "<", dest])

    def process_part(self, part):
        for condition in self.conditions:
            if len(condition) == 1:
                self.set_dest(part, condition[0])
                return
            else:
                if condition[2] == "<":
                    if part.stats[condition[0]][0] < condition[1] and part.stats[condition[0]][1] >= condition[1]:
                        copy_part_stats = deepcopy(part.stats)
                        copy_part_stats[condition[0]][1] = condition[1] - 1
                        self.set_dest(Part(copy_part_stats, ""), condition[3])
                        part.stats[condition[0]][0] = condition[1]
                    elif part.stats[condition[0]][1] < condition[1]:
                        self.set_dest(part, condition[3])
                        return
                else:
                    if part.stats[condition[0]][0] < condition[1] and part.stats[condition[0]][1] >= condition[1]:
                        copy_part_stats = deepcopy(part.stats)
                        copy_part_stats[condition[0]][0] = condition[1] + 1
                        self.set_dest(Part(copy_part_stats, ""), condition[3])
                        part.stats[condition[0]][1] = condition[1]
                    elif part.stats[condition[0]][0] > condition[1]:
                        self.set_dest(part, condition[3])
                        return

                # if part.stats[condition[0]] * condition[2] > condition[1] * condition[2]:
                #     self.set_dest(part, condition[3])
                #     return

    def set_dest(self, part, dest):
        if dest == "R":
            part.accepted = False
        elif dest == "A":
            part.accepted = True
        else:
            part.workflow = dest
        created_parts.append(part)

class Part:
    def __init__(self, stats, workflow):
        self.accepted = None
        self.workflow = workflow
        self.stats = stats

    def get_score(self):
        score = 1
        for ranges in self.stats.values():
            score *= (ranges[1] - ranges[0] + 1)
        return score

with open("data/D19.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

workflows = {}
building_workflows = True
score = 0
open_parts = []
for line in input:
    if line == "":
        open_parts.append(Part({"x":[1, 4000], "m":[1, 4000], "a":[1, 4000], "s":[1, 4000]}, "in"))
        while len(open_parts) > 0:
            new_open_parts = []
            for part in open_parts:
                created_parts = []
                workflows[part.workflow].process_part(part)
                for created_part in created_parts:
                    #print(created_part.stats)
                    if created_part.accepted != None:
                        if created_part.accepted:
                            score += created_part.get_score()
                    else:
                        new_open_parts.append(created_part)
            open_parts = new_open_parts
        break
    else:
        name = line[:line.index("{")]
        conditions = line[line.index("{") + 1:-1]
        workflows[name] = Workflow(conditions)

print(score)
