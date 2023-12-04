import numpy as np
def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    return data

lines = get_data('task.txt')
lines = [x.rstrip() for x in lines]

total = 0
all_cards = np.zeros(len(lines))
all_cards += 1
for i, line in enumerate(lines):
    cardno, numbers = line.split(': ')
    tickets, results = numbers.split(' | ')
    tickets = tickets.split()
    results = results.split()

    correct_nums = len(list(set(tickets) & set(results)))
    all_cards[i+1: i + correct_nums + 1] += all_cards[i] * 1
    if correct_nums > 0:
        total +=  pow(2,correct_nums - 1)

print('Task 1:', total)
print('Task 2:', sum(all_cards))
