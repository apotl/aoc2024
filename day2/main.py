reports = []

with open("input.txt") as f:
    for line in f:
        reports += [[int(x) for x in line.split()]]

safe_count_pt1 = 0
safe_count_pt2 = 0

def is_report_safe(report: list):
    is_safe = True
    prev_dif = None
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if abs(difference) < 1 or abs(difference) > 3:
            is_safe = False
            break
        if prev_dif is not None:
            if difference * prev_dif < 0:
                is_safe = False
                break
        prev_dif = difference

    return is_safe

for report in reports:
    if not is_report_safe(report):
        removed_permutations = [report[:x-1]+report[x:] for x in range(1, len(report)+1)]
        result = [is_report_safe(r) for r in removed_permutations]
        if True not in result:
            continue
    else:
        safe_count_pt1 += 1
    safe_count_pt2 += 1
print(safe_count_pt1, safe_count_pt2)
