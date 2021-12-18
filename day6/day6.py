import numpy as np
import time

def get_data(fname):
    return np.loadtxt(fname, delimiter=',')

def new_day(fish_l):
    return fish_l-1
	
def go_days1(f_list, days):
    for i in range(days):
        ind = np.where(f_list == 0)
        if len(ind[0]) > 0:
            f_list[ind] = 7
            for i in range(len(ind[0])):
                f_list = np.append(f_list, 9)
        f_list = new_day(f_list)
    return f_list

def go_days2(f_list, days):
    for i in range(days):
        print(i)
        ind = np.where(f_list == 0)
        if len(ind[0]) > 0:
            f_list[ind] = 7
            f_list = np.concatenate((f_list,[9]*len(ind[0])))
        f_list = new_day(f_list)
    return f_list
	
fishies = get_data('input.txt')
start = time.time()
fishies = go_days2(fishies, 256)
print(len(fishies))
end = time.time()
print(end - start)
