#!usr/bin/python3
import random


n,s = [int(x) for x in input().split()]
for j in range(n):
    current_position = random.choice([0,1])
    loc = [0, 0]
    iter = 0
    ac = 0
    flag = False

    for i in range(s):
        i = input()[1:-1].split(', ')
        location = (int(i[0][1:]), int(i[1][:1]))
        loc[location[0]] = (1 if i[2][1:-1] == 'Dirty' else 0) # status

        if loc[current_position] == 1:
            loc[current_position] = 0
            flag = True
            print('Suck')

        elif (ac == 0) or (ac == 1 and flag):
            if current_position == 0: print('Left')
            else: print('Right')

        elif sum(loc) == 0 and iter < 8: 
            print('NoOp')

        elif loc[current_position] == 0 and current_position == 0:
            iter = 0
            current_position = 1
            print('Right')

        elif loc[current_position] == 0 and current_position == 1:
            iter = 0
            current_position = 0 
            print('Left')
        
        iter += 1
        ac += 1
