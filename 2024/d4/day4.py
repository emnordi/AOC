with open('input.txt') as f:
    s = f.readlines()

def is_xmas(inp):
    return inp == 'XMAS' or inp[::-1] == 'XMAS'

def is_mas(inp):
    return inp == 'MAS' or inp[::-1] == 'MAS'

hits_count = 0
hits_count2 = 0

for y in range(len(s)):
    for x in range(len(s[y])):
        if s[y][x] == 'X':
            #right
            if is_xmas(s[y][x:x+4]):
                hits_count += 1
            #left
            if is_xmas(s[y][x-3:x+1]):
                hits_count += 1
            #up
            if y > 2 and is_xmas(''.join([s[y-i][x] for i in range(4)])):
                hits_count += 1
            #down
            if y < len(s) - 3 and is_xmas(''.join([s[y+i][x] for i in range(4)])):
                hits_count += 1
            #diag right down
            if y < len(s) - 3 and x < len(s[y]) - 3 and is_xmas  (''.join([s[y+i][x+i] for i in range(4)])):
                hits_count += 1
            #diag left down
            if y < len(s) - 3 and x > 2 and is_xmas(''.join([s[y+i][x-i] for i in range(4)])):
                hits_count += 1
            #diag right up
            if y > 2 and x < len(s[y]) - 3 and is_xmas(''.join([s[y-i][x+i] for i in range(4)])):
                hits_count += 1
            #diag left up
            if y > 2 and x > 2 and is_xmas(''.join([s[y-i][x-i] for i in range(4)])):
                hits_count += 1

for y in range(len(s)):
    for x in range(len(s[y])):
        if s[y][x] == 'A':
            if x > 0 and y > 0 and x < len(s[y]) - 1 and y < len(s) - 1 and is_mas(''.join([s[y-1+i][x-1+i] for i in range(3)])):
                if x < len(s[y]) - 1 and y > 0 and is_mas(''.join([s[y-1+i][x+1-i] for i in range(3)])):
                    hits_count2 += 1
            
print(hits_count)
print(hits_count2)