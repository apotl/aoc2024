list1 = []
list2 = []
with open("input.txt") as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

list1 = sorted(list1)
list2 = sorted(list2)

if len(list1) != len(list2):
    print("length mismatch")
    exit(1)

sum = 0
histo = {}
for i in range(len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))

    if histo.get(list1[i]) == None:
        histo[list1[i]] = 0

    i += 1

print(sum)
for i in range(len(list1)):
    if histo.get(list2[i]) is not None:
        histo[list2[i]] += 1
    i += 1

simul_score = 0
for num, occur in histo.items():
    simul_score += num * occur

print(simul_score)