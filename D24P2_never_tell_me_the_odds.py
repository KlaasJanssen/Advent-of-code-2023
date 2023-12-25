from math import sqrt
import sys
from collections import defaultdict

class Hail_Stone:
    def __init__(self, pos, vel):
        self.pos = [int(x) for x in pos.split(", ")]
        self.vel = [int(x) for x in vel.split(", ")]

        for index, x in enumerate(self.vel):
            a[index][x] += 1

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

a = [defaultdict(int), defaultdict(int), defaultdict(int)]
with open("data/D24.txt", "r") as f:
#with open("test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

hail_stones = []
for line in input:
    hail_stones.append(Hail_Stone(*line.split(" @ ")))


# for dct in a:
#     print(max(dct.items(), key = lambda x: x[1]))

# for dct in a:
#     print([x for x in dct.items() if x[1] > 1])
direction = []
for index_1 in range(3):
    possible_vels = set(range(-1000, 1001))
    for vels in a[index_1].items():
        hail_subset = [x for x in hail_stones if x.vel[index_1] == vels[0]]
        for index, hail1 in enumerate(hail_subset[:-1]):
            for hail2 in hail_subset[index + 1:]:
                pos_check = possible_vels.copy()
                for check in pos_check:
                    if check - vels[0] != 0:
                        if abs(hail1.pos[index_1] - hail2.pos[index_1]) % abs(vels[0] - check) != 0:
                            possible_vels.remove(check)

    direction.append(list(possible_vels)[0])

print(direction)

hail_subset = [x for x in hail_stones if x.vel[0] == 156]
x_dist = hail_subset[1].pos[0] - hail_subset[0].pos[0]
dt = x_dist / (direction[0] - hail_subset[0].vel[0])

print(hail_subset[0].pos[0] + direction[0] * dt == hail_subset[1].pos[0] + hail_subset[1].vel[0]*dt)
t = (hail_subset[1].pos[1] + hail_subset[1].vel[1] * dt - hail_subset[0].pos[1] - direction[1] * dt) / (hail_subset[0].vel[1] - hail_subset[1].vel[1])
#t = (y2 + y_vel2 * dt - y1 - dir[1] * dt) / (y_vel1 - y_vel2)
print(t)
print(hail_subset[0].pos[1] + hail_subset[0].vel[1] * t + direction[1] * dt == hail_subset[1].pos[1] + hail_subset[1].vel[1] * (t + dt))
#print(hail_subset)
a = hail_subset[0].pos[1] + hail_subset[0].vel[1] * t - direction[1] * t
b = hail_subset[0].pos[0] + hail_subset[0].vel[0] * t - direction[0] * t
c = hail_subset[0].pos[2] + hail_subset[0].vel[2] * t - direction[2] * t
# print(hail_subset[0].pos[1] + hail_subset[0].vel[1] * t - direction[1] * t)
# print(hail_subset[0].pos[0] + hail_subset[0].vel[0] * t - direction[0] * t)
# print(hail_subset[0].pos[2] + hail_subset[0].vel[2] * t - direction[2] * t)
print(a + b + c)
# score = 0
# for index, stone1 in enumerate(hail_stones[:-1]):
#     for stone2 in hail_stones[index + 1:]:
#         collision_pos = stone1.get_collision(stone2)
#         #print(collision_pos)
#         #if collision_pos[0] >= 7 and collision_pos[0] <= 27 and collision_pos[1] >= 7 and collision_pos[1] <= 27:
#         if collision_pos[0] >= 2e14 and collision_pos[0] <= 4e14 and collision_pos[1] >= 2e14 and collision_pos[1] <= 4e14:
#             score += 1
#
# print(score)
