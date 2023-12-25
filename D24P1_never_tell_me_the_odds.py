from math import sqrt
import sys

class Hail_Stone:
    def __init__(self, pos, vel):
        self.pos = [int(x) for x in pos.split(", ")][:2]
        self.vel = [int(x) for x in vel.split(", ")][:2]

        self.a = self.vel[1] / self.vel[0]
        self.b = self.pos[1] - (self.vel[1] * self.pos[0] / self.vel[0])
        #print(f"y = {self.a}x + {self.b}")

    def get_collision(self, other):
        if self.a == other.a:
            return [0,0]
        collision_x = (other.b - self.b) / (self.a - other.a)
        time1 = (collision_x - self.pos[0]) / self.vel[0]
        time2 = (collision_x - other.pos[0]) / other.vel[0]
        if time1 < 0 or time2 < 0:
            return [0,0]

        collision_y = self.pos[1] + self.vel[1] * time1
        return [collision_x, collision_y]


with open("data/D24.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

hail_stones = []
for line in input:
    hail_stones.append(Hail_Stone(*line.split(" @ ")))

score = 0
for index, stone1 in enumerate(hail_stones[:-1]):
    for stone2 in hail_stones[index + 1:]:
        collision_pos = stone1.get_collision(stone2)
        #print(collision_pos)
        #if collision_pos[0] >= 7 and collision_pos[0] <= 27 and collision_pos[1] >= 7 and collision_pos[1] <= 27:
        if collision_pos[0] >= 2e14 and collision_pos[0] <= 4e14 and collision_pos[1] >= 2e14 and collision_pos[1] <= 4e14:
            score += 1

print(score)
