import re
sum_pt1 = 0
compiled_regex_mul = re.compile(r"mul\((\d*),(\d*)\)")
with open("input.txt") as f:
    for line in f:
        matches = re.findall(compiled_regex_mul, line)
        sum_pt1 += sum([int(x[0])*int(x[1]) for x in matches])
print(sum_pt1)

sum_pt2 = 0
compiled_regex_dodonts = re.compile(r'do\(\)|don\'t\(\)|mul\(\d*,\d*\)')
with open("input.txt") as f:
    matches = []
    enabled = True
    for line in f:
        matches += re.findall(compiled_regex_dodonts, line)
    for i in range(len(matches)):
        if matches[0] == "do()":
            enabled = True
        elif matches[0] == "don't()":
            enabled = False
        elif enabled == True:
            result = compiled_regex_mul.findall(matches[0])
            if len(result) > 0:
                sum_pt2 += int(result[0][0]) * int(result[0][1])
        matches.pop(0)
print(sum_pt2)