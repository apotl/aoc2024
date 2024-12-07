map = []

with open('input.txt') as f:
    for line in f:
        map.append([c for c in line.strip()])

def find_guard(map: list[list]) -> tuple[int,int]:
    row_num = 0
    for line in map:
        if '^' in line:
            return row_num, line.index('^')
        row_num += 1

directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

MAX_LOOP = 4
def run_simul(obstruction: tuple[int]  =None) -> dict[tuple,list]:
    direction_index = 0
    covered_locs : dict[tuple,list] = {}
    guard_loc = find_guard(map)
    steps = 0
    covered_locs[guard_loc] = [steps]

    while 1:
        try:
            pos_guard_loc = guard_loc[0]+directions[direction_index][0], guard_loc[1]+directions[direction_index][1]
            if map[pos_guard_loc[0]][pos_guard_loc[1]] == '#' or (obstruction and obstruction[0] == pos_guard_loc[0] and obstruction[1] == pos_guard_loc[1]):
                direction_index += 1
                if direction_index > 3:
                    direction_index = 0
            guard_loc = guard_loc[0]+directions[direction_index][0], guard_loc[1]+directions[direction_index][1]
            if guard_loc[0] < 0 or guard_loc[1] < 0:
                raise IndexError
            #print(guard_loc)
            steps += 1
            if not covered_locs.get(guard_loc):
                covered_locs[guard_loc] = []
            covered_locs[guard_loc].append(steps)
            if len(covered_locs[guard_loc]) > MAX_LOOP:
                break
        except IndexError:
            break
    return covered_locs

vanilla_simul = run_simul()
ans_pt1 = len(vanilla_simul.keys())
print(ans_pt1)

#print(sum([len(v) for k, v in covered_locs.items() if len(v) > 1]))
raise NotImplementedError
ans_pt2 = 0
for obstruction in vanilla_simul.keys() - find_guard(map):
    try:
        #print(obstruction)
        simul = run_simul(obstruction=obstruction)
        result = [len(v) for k, v in simul.items() if len(v) > MAX_LOOP]
        ans_pt2 += 1 if sum(result) > 0 else 0
        #print(result)

    except IndexError:
        break
print(ans_pt2)