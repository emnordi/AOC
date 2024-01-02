import numpy as np
def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip().split() for line in lines]
		
data = get_data('task.txt')
base = np.zeros((347, 373))
curx = 0
cury = 144
for instr in data:
    d, steps, colour = instr
    if d == 'R':
        base[cury][curx:curx+int(steps)+1] = 1
        curx = curx+int(steps)
    if d == 'L':
        base[cury][curx-int(steps):curx+1] = 1
        curx = curx-int(steps)
    if d == 'U':
        base[cury-int(steps):cury+1, curx] = 1
        cury = cury-int(steps)
    if d == 'D':
        base[cury:cury+1+int(steps), curx] = 1
        cury = cury+int(steps)
np.set_printoptions(linewidth=400)
for b in base:
    print(''.join([str(l) for l in list(b.astype(int))]).replace('0', '.'))