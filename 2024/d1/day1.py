def get_data(fname):
    list1 = []
    list2 = []
    with open(fname) as f:
        for line in f:
            v1, v2 = line.split()
            list1.append(int(v1))
            list2.append(int(v2))
    list1.sort()
    list2.sort()
    return list1, list2

l1, l2 = get_data('input.txt')

task1_total = 0
task2_total = 0

for i, j in zip(l1, l2):
    task1_total += abs(i - j)
    task2_total += i*l2.count(i)

print('Task 1 result:', task1_total)
print('Task 2 result:', task2_total)