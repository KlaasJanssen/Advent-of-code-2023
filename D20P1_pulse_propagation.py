class Broadcaster:
    def __init__(self, dest):
        self.name = "broadcaster"
        self.destinations = dest.split(", ")

    def process_signal(self, origin, strength):
        for dest in self.destinations:
            queue.append((dest, self.name, strength))

class FlipFlop:
    def __init__(self, dest, name):
        self.name = name
        self.destinations = dest.split(", ")
        self.on = False

    def process_signal(self, origin, strength):
        if strength == "low":
            self.on = not self.on

            if self.on:
                for dest in self.destinations:
                    queue.append((dest, self.name, "high"))
            else:
                for dest in self.destinations:
                    queue.append((dest, self.name, "low"))

class Remember:
    def __init__(self, dest, name):
        self.name = name
        self.destinations = dest.split(", ")
        self.connections = {}

    def process_signal(self, origin, strength):
        self.connections[origin] = strength

        send_low = True
        for value in self.connections.values():
            if value == "low":
                send_low = False
                break

        strength = "low" if send_low else "high"
        for dest in self.destinations:
            queue.append((dest, self.name, strength))

def send_signal(dest, origin, strength):
    signals_sent[strength] += 1
    if dest in modules.keys():
        modules[dest].process_signal(origin, strength)


with open("data/D20.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

modules = {}
for line in input:
    split_line = line.split(" -> ")
    if split_line[0] == "broadcaster":
        modules["broadcaster"] = Broadcaster(split_line[1])
    elif split_line[0][0] == "%":
        modules[split_line[0][1:]] = FlipFlop(split_line[1], split_line[0][1:])
    elif split_line[0][0] == "&":
        modules[split_line[0][1:]] = Remember(split_line[1], split_line[0][1:])

for key, value in modules.items():
    for dest in value.destinations:
        if dest in modules.keys():
            if isinstance(modules[dest], Remember):
                modules[dest].connections[key] = "low"

signals_sent = {"low":0, "high":0}
for x in range(1000):
    queue = [("broadcaster", "button", "low")]
    while len(queue) > 0:
        signal = queue.pop(0)
        #print(signal)
        send_signal(*signal)

print(signals_sent["high"] * signals_sent["low"])
