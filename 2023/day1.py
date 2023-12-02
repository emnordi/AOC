def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    return data

def find_first_number(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return i
    return -1

def replace_nums(line):
    line = line.replace('one', 'one1one')
    line = line.replace('two', 'two2two')
    line = line.replace('three', 'three3three')
    line = line.replace('four', 'four4four')
    line = line.replace('five', 'five5five')
    line = line.replace('six', 'six6six')
    line = line.replace('seven', 'seven7seven')
    line = line.replace('eight', 'eight8eight')
    line = line.replace('nine', 'nine9nine')
    return line

lines = get_data('task1.txt')

total = 0
for line in lines:
    first = find_first_number(line)
    last = find_first_number(line[::-1])
    total += int(line[first] + line[::-1][last])

print("task 1: ", total)

total = 0

for line in lines:
    lineM = replace_nums(line)
    first = find_first_number(lineM)
    last = find_first_number(lineM[::-1])
    total += int(lineM[first] + lineM[::-1][last])

print("task 2: ", total)