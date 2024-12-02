def get_data(fname):
    list1 = []
    with open(fname) as f:
        for line in f:
            temp = line.split()
            list1.append([int(i) for i in temp])
    return list1

def safe_line(inp):
    asc = None
    for i in range(len(inp)-1):
            current_asc = inp[i] < inp[i+1]
            if asc is None:
                asc = current_asc
            if inp[i] == inp[i+1] or (not current_asc and asc) or (current_asc and not asc):
                return False, i
            if abs(inp[i] - inp[i+1]) > 3:
                return False, i
    return True, None

l1 = get_data('input.txt')

task1_total = 0
task2_total = 0
 
for l in l1:
    safe, i = safe_line(l)
    if safe:
        task1_total += 1
        task2_total += 1
    elif i is not None:
        s1, _ = safe_line(l[:i] + l[i+1:])
        s2, _ = safe_line(l[:i+1] + l[i+2:])
        s3, _ = safe_line(l[:i-1] + l[i:])
        if s1 or s2 or s3:
            task2_total += 1

print('Task 1 result:', task1_total)
print('Task 2 result:', task2_total)