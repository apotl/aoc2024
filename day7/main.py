equations = []

import itertools

with open('input.txt') as f:
    for line in f:
        equations += [(int(line.split(":")[0]), [int(x) for x in line.split(": ")[1].split()])]

def try_perms(eqs, operators):
    sum_valid = 0
    for eq in eqs:
        print(".", end='', flush=True)
        i_max = len(eq[1])-1
        permutations = list(itertools.product( operators, repeat=i_max))
        possible_values = []
        for p in permutations:
            pos_val = eq[1][0]
            i = 0
            while i < i_max:
                if p[i] == '*':
                    pos_val *= eq[1][i+1]
                    i += 1
                elif p[i] == '+':
                    pos_val += eq[1][i+1]
                    i += 1
                elif p[i] == '||':
                    pos_val = int(str(pos_val)+str(eq[1][i+1]))
                    i += 1
                else:
                    raise
            possible_values += [pos_val]
        if eq[0] in possible_values:
            eq += (possible_values[possible_values.index(eq[0])],)
            sum_valid += eq[0]
    return sum_valid

ans_pt1 = try_perms(equations, ["+", "*"])
print(ans_pt1)
ans_pt2 = try_perms(equations, ["+", "*", "||"])
print(ans_pt2)