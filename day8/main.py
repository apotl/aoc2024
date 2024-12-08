map = []
from itertools import combinations
with open('input.txt') as f:
    for line in f:
        map.append([c for c in line.strip()])

nodes = {}

max_x = len(map) - 1
max_y = len(map[0]) - 1

for x in range(len(map)):
    for y in range(len(map[0])):
        p = map[x][y]
        if p == '.':
            continue
        if not nodes.get(p):
            nodes[p] = []
        nodes[p] += [(x,y)]

def f(x, m, b):
    return round(m*x + b)

def is_point_in_map(p):
    if (p[0] >= 0 and p[0] <= max_x) and (p[1] >= 0 and p[1] <= max_y):
        return True
    return False


def find_antinodes(pt2_flag=False):
    antinodes = {}
    for k, v in nodes.items():
        pairs = list(combinations(v, 2))
        for p_1, p_2 in sorted(pairs, key=lambda k: k[0]):
            dy = p_2[1] - p_1[1]
            dx = p_2[0] - p_1[0]
            a_ps : list[tuple] = []
            if dx == 0:
                a_ps +=[ (p_1[0], p_1[1] - dy)]
                a_ps +=[ (p_2[0], p_2[1] + dy)]

                if pt2_flag:
                    i = 2
                    while is_point_in_map(p_1[0], p_1[1] - i*dy):
                        a_ps +=[ (p_1[0], p_1[1] - i*dy)]
                        i += 1
                    i = 2
                    while is_point_in_map(p_2[0], p_2[1] + i*dy):
                        a_ps +=[ (p_2[0], p_2[1] + i*dy)]
                        i += 1


            else:
                m = dy / dx
                b = p_1[1] - m * p_1[0]

                a_ps += [(p_1[0] - dx, f(p_1[0] - dx, m, b))]
                a_ps += [(p_2[0] + dx, f(p_2[0] + dx, m, b))]

                if pt2_flag:
                    i = 0
                    while is_point_in_map((p_1[0] - i*dx, f(p_1[0] - i*dx, m, b))):
                        a_ps +=[ (p_1[0] - i*dx, f(p_1[0] - i*dx, m, b))]
                        i += 1
                    i = 0
                    while is_point_in_map((p_2[0] + i*dx, f(p_2[0] + i*dx, m, b))):
                        a_ps +=[ (p_2[0] + i*dx, f(p_2[0] + i*dx, m, b)) ]
                        i += 1

            for a in a_ps:
                if is_point_in_map(a):
                    if not antinodes.get(a):
                        antinodes[a] = []
                    antinodes[a] += [k]
    return antinodes

ans_pt1 = len(find_antinodes().keys())
print(ans_pt1)


ans_pt2 = len(find_antinodes(pt2_flag=True).keys())
print(ans_pt2)
