import sys

with open('input.txt') as f:
    rules = []
    sections = []
    lines = f.readlines()
    for line in lines:
        if '|' in line:
            rule = line.rstrip().split('|')
            rules.append(rule)
        else:
            if line == '\n':
                continue
            sections.append(line.rstrip().split(','))

def rules_for_section(section):
    relevant_rules = []
    for [x, y] in rules:
        if x in section and y in section:
            relevant_rules.append([x, y])
    return relevant_rules

def is_before(inp, section):
    inp_index = section.index(inp)
    for [x, y] in rules:
        i = section.index(y) if y in section else inp_index + 1
        if inp == x and i < inp_index:
            return False
    return True

def check_section(section):
    for i in range(len(section)):
        if not is_before(section[i], section):
            return False
    return True

def is_x_before_y(x, y, rule_section):
    ans = False
    for [a, b] in rule_section:
        if a == x and b == y or (a == x and is_x_before_y(b, y, rule_section)):
            return True
    return ans


def order_section(section):
    ordered = [section[0]]
    rule_section = rules_for_section(section)
    for i in range(len(section[1:])):
        for o in ordered:
            if is_x_before_y(section[i+1], o, rule_section):
                ordered.insert(ordered.index(o), section[i+1])
                break
        if section[i+1] not in ordered:
            ordered.append(section[i+1])
    return ordered

sum = 0
bad_sections = []
for section in sections:
    if check_section(section):
        sum += int(section[len(section) // 2])
    else:
        bad_sections.append(section)

sum2 = 0

for section in bad_sections:
    ordered_section = order_section(section)
    sum2 += int(ordered_section[len(ordered_section) // 2])


print('Task 1:', sum)
print('Task 2:', sum2)
