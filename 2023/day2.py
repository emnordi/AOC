def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    return data

lines = get_data('task2.txt')

max_red = 12
max_green = 13
max_blue = 14

def legal_game(r):
    count_dict = {'red': 0, 'green': 0, 'blue': 0}
    outcomes = ''.join(r).split(', ')
    for o in outcomes:
        amount, color = o.split(' ')
        count_dict[color] += int(amount)
    if count_dict['red'] > max_red or count_dict['green'] > max_green or count_dict['blue'] > max_blue:
        return False
    return True

def mul(li):
    total = 1
    for i in li:
        total *= i
    return total

def count_min_dice_for_game(r):
    count_dict = {'red': 0, 'green': 0, 'blue': 0}
    outcomes = ', '.join(r).split(', ')
    for o in outcomes:
        amount, color = o.split(' ')
        if count_dict[color] < int(amount):
            count_dict[color] = int(amount)
    return mul(count_dict.values())

def task1():
    legal_games = []
    for line in lines:
        gameno, gamedata = line.rstrip().split(': ')
        gameno = gameno.split(' ')[1]
        roundresults = gamedata.split('; ')
        legal = True
        for ro in roundresults:
            if (not legal_game(ro)):
                legal = False
                break
        if legal:
            legal_games.append(gameno)

    total = sum([int(x) for x in legal_games])
    print('Task1', total)

def task2():
    total = 0
    for line in lines:
        _, gamedata = line.rstrip().split(': ')
        roundresults = gamedata.split('; ')
        total += count_min_dice_for_game(roundresults)
    print('Task2', total)


task1()
task2()

