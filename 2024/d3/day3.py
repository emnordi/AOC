
with open('input.txt') as f:
    f = f.read().strip()

do_commands = f.split('do()')

task2_inp = ''

for d in do_commands:
    x = d.split("don't")
    task2_inp += x[0]

def do_mult(in_str):
    total = 0
    all_muls = in_str.split('mul(')[1:]
    for v in all_muls:
        if ')' not in v:
            continue
        pair = v.split(')')[0]
        if ',' not in pair:
            continue
        x,y = pair.split(',')
        if x.isnumeric() and y.isnumeric():
            total += int(x)*int(y)
    return total

task1 = do_mult(f)

task2 = do_mult(task2_inp)

print('Task1: ' + str(task1))

print('Task2: ' + str(task2))