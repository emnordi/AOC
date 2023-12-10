import sys
sys.setrecursionlimit(100000000)

def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
        
def can_go_north(d, x, y):
    if y != 0 and d[y][x] in 'S|LJ' and d[y-1][x] in 'S|7F':
        return True
    return False
    
def can_go_east(d, x, y):
    if x != len(d[y])-1 and d[y][x] in 'S-LF' and d[y][x+1] in 'S-J7':
        return True
    return False
    
def can_go_south(d, x, y):
    if y != len(d)-1 and d[y][x] in 'S|7F' and d[y+1][x] in 'S|LJ':
        return True
    return False
    
def can_go_west(d, x, y):
    if x != 0 and d[y][x] in 'S-J7' and d[y][x-1] in 'S-LF':
        return True
    return False
    
def go_on(x, y, visited, d):
    return (d[y][x] == 'S' and len(visited) > 2) or [x, y] not in visited

def find_path(d, x, y):
    curr_x = x
    curr_y = y
    visited = []
    while True:
        visited.append([curr_x, curr_y])
        #print(d[curr_y][curr_x])
        if d[curr_y][curr_x] == 'S' and len(visited) > 2:
            return visited
        if can_go_north(d, curr_x, curr_y) and go_on(curr_x, curr_y-1, visited, d):
            curr_y -= 1
        elif can_go_east(d, curr_x, curr_y) and go_on(curr_x+1, curr_y, visited, d):
            curr_x += 1
        elif can_go_south(d, curr_x, curr_y) and go_on(curr_x, curr_y+1, visited, d):
            curr_y += 1
        elif can_go_west(d, curr_x, curr_y) and go_on(curr_x-1, curr_y, visited, d):
            curr_x -= 1

def get_start(data):
    for y, d in enumerate(data):
        if 'S' in d:
            return [d.index('S'), y]
            
data = get_data('task.txt')
start_pos = get_start(data)

res = find_path(data, start_pos[0], start_pos[1])
print('Task1:', (len(res)-1) /2)

data2 = data
for r in res:
    x, y = r
    temp = list(data2[y])
    temp[x] = '█'
    data2[y] = ''.join(temp)
    
for y, d in enumerate(data2):
    for x, c in enumerate(d):
        if c == '█':
            break
        else:
            temp = list(data2[y])
            temp[x] = '0'
            data2[y] = ''.join(temp)
           
for y, d in enumerate(data2):
    ind = d.rfind('█')
    if ind != -1:
        temp = list(data2[y])
        data2[y] = ''.join(temp[:ind])
    
for d in data2:
    print(d)