import time

def get_data(fname):
    with open(fname) as f:
        lines = f.readline()
        print(lines)
        #for line in lines:
        #    fish[int(line)] += 1

fish = [0,0,0,0,0,0,0,0,0]
lines = get_data('input.txt')

print(fish)
#start = time.time()
#fishies = go_days2(fishies, 256)
#print(len(fishies))
#end = time.time()
#print(end - start)
