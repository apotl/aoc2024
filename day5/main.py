rules = []
pagelists = []

with open("day5/input.txt") as f:
    a, b = f.read().split('\n\n')

    for line in a.split('\n'):
        rules += [[int(x) for x in line.split('|')]]

    for line in b.split('\n'):
        pagelists += [[int(x) for x in line.split(",")]]

def is_correctly_ordered(pagelist: list):
    for rule in rules:
        if rule[0] not in pagelist or rule[1] not in pagelist:
            continue
        if pagelist.index(rule[0]) > pagelist.index(rule[1]):
            return False
        
    return True

def correct_page_order(pagelist: list) -> list:
    for rule in rules:
        if rule[0] not in pagelist or rule[1] not in pagelist:
            continue
        if pagelist.index(rule[0]) > pagelist.index(rule[1]):
            pagelist[pagelist.index(rule[0])], pagelist[pagelist.index(rule[1])] = pagelist[pagelist.index(rule[1])], pagelist[pagelist.index(rule[0])]
            #print(pagelist)
    
    if not is_correctly_ordered(pagelist):
        pagelist = correct_page_order(pagelist)

    return pagelist



ans_pt1 = 0
for p in pagelists:
    if is_correctly_ordered(p):
        ans_pt1 += p[int(len(p) / 2)]

print(ans_pt1)

ans_pt2 = 0 
for p in pagelists:
    #print(p)
    if is_correctly_ordered(p):
        ans_pt2 += p[int(len(p) / 2)]
        ans_pt2 -= p[int(len(p) / 2)]
    else:
        p = correct_page_order(p)
        if is_correctly_ordered(p):
            #print("fixed", p[int(len(p) / 2)])
            ans_pt2 += p[int(len(p) / 2)]

print(ans_pt2)