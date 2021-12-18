import numpy as np 

def check_vents(vents):
	rows, cols = np.where(vents > 1)
	return len(rows)

def get_input():
	arr = []
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			fr, to = line.split(' -> ')
			x1, y1 = fr.split(',')
			x2, y2 = to.split(',')
			arr.append([(int(x1),int(y1)), (int(x2),int(y2))])
		return arr

def get_max_val(arr):
	return np.amax(arr)

def create_vents_map(maxval):
	return np.zeros((maxval, maxval))

def add_vents(ventsmap, c1, c2):
	x1, y1 = c1
	x2, y2 = c2
	if x1 == x2:
		for i in range(min(y1, y2), max(y1, y2)+1):
			ventsmap[i][x1] += 1
	elif y1 == y2:
		for i in range(min(x1, x2), max(x1, x2)+1):
			ventsmap[y1][i] += 1
	return ventsmap

coords = get_input()
maxval = get_max_val(coords)
ventsmap = create_vents_map(maxval+1)

for c1, c2 in coords:
	ventsmap = add_vents(ventsmap, c1, c2)

print(check_vents(ventsmap))