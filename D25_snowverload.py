from collections import defaultdict

# class Module:
#     def __init__(self, name, connections):
#         self.name = name
#         self.connections = []
#         for connection in connections.split(" "):
#             self.connections.append(connection)
#             if connection in modules.keys():
#                 connection.connections.append(name)
#             else:
#                 modules[connection] = Module(connection, self.name)

with open("data/D25.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

# with open("graphviz_input.dot", "w") as f:
#     f.write("graph D {\n")
#     for line in input:
#         f.write(line.replace(": ", " -- {").replace(", ", "") + "}\n")
#     f.write("}")

modules = defaultdict(set)

for line in input:
    name, connections = line.split(": ")
    for connection in connections.split(" "):
        modules[name].add(connection)
        modules[connection].add(name)

modules["qns"].remove("jxm")
modules["jxm"].remove("qns")
modules["tjd"].remove("dbt")
modules["dbt"].remove("tjd")
modules["mgb"].remove("plt")
modules["plt"].remove("mgb")

group = set()
group.add("qns")

open = ["qns"]
while len(open) > 0:
    new_open = []
    for module in open:
        for connection in modules[module]:
            if not connection in group:
                group.add(connection)
                new_open.append(connection)
    open = new_open
    
print(len(group) * (len(modules) - len(group)))
