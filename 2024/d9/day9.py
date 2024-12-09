import re
import time

def get_data(fname):
    with open(fname) as f:
        line = f.readline().strip()
        pairs = re.findall('..?', line)
        return_pairs = []
        for i, p in enumerate(pairs):
            if len(p) == 2:
                return_pairs.append([int(p[0]), int(p[1]), i])
            else:
                return_pairs.append([int(p), 0, i])
        return return_pairs            

def get_files(data):
    total = []
    for d in data:
        if len(d) > 2:
            num, space, ind = d
            total += [ind] * num
            total += [None] * space
        else:
            total += [d[1]] * d[0]
    return total


def task_1(files):
    result = 0
    for i, t in enumerate(files):
        if t == None:
            last_el = files.pop()
            while(last_el == None):
                last_el = files.pop()
            files[i] = last_el
            result += last_el*i
        else:
            result += t*i
    return result

def task_2(files, data):
    for size, _, file_id in reversed(data):
        start_index = files.index(file_id)
        end_index = start_index + size

        free_start = None
        free_count = 0

        for i in range(len(files)):
            if files[i] is None:
                if free_start is None:
                    free_start = i
                free_count += 1
                if free_count == size:
                    if free_start < start_index:
                        # Remove file from old location
                        for j in range(start_index, end_index):
                            files[j] = None
                        # Put file in new location
                        for j in range(free_start, free_start + size):
                            files[j] = file_id
                    break
            else:
                free_start = None
                free_count = 0
    
    result = 0
    for i, t in enumerate(files):
        if t != None:
            result += t*i
    return result


data = get_data('input.txt')
files = get_files(data)
print('Task1:', task_1(files.copy()))
start_time = time.time()
print('Task2:', task_2(files.copy(), data))
print("--- %s seconds ---" % (time.time() - start_time))