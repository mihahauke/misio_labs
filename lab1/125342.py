#!usr/bin/python3
import random

n,s = [int(x) for x in input().split()]
memory = [[],[]]
for j in range(n):
    current_position = 0 #random.choice([0,1])
    loc = [0, 0]

    for i in range(s):
        i = input()[1:-1].split(', ')
        location = (int(i[0][1:]), int(i[1][:1]))
        loc[location[0]] = (1 if i[2][1:-1] == 'Dirty' else 0) # status

        memory[0].append(location)
        memory[1].append(loc[location[0]])

        length = len(memory[1])
        sumup = sum(memory[1])
        probability = sumup / length

        # # print stats
        # for k,m in zip(memory[0],memory[1]):
        #     print(k," - ",m)
        # print("current position: ", current_position)
        # print("loc: ", loc)
        # print("prob: ", probability)      

        # if clean and clen -> noOp

        if length < 100:
            if loc[current_position] == 1:
                loc[current_position] = 0
                print('Suck')

            elif loc[current_position] == 0 and current_position == 0:
                decide = random.uniform(0,1)
                if decide < 0.15:
                    current_position = 1
                    print('Right')
                else:
                    print('NoOp')

            elif loc[current_position] == 0 and current_position == 1:
                decide = random.uniform(0,1)
                if decide < 0.15:
                    current_position = 0 
                    print('Left')
                else: 
                    print('NoOp')
        
        else:
            if loc[current_position] == 1:
                loc[current_position] = 0
                print('Suck')

            elif loc[current_position] == 0 and current_position == 0:
                decide = random.uniform(0,1)
                if decide < probability:
                    current_position = 1
                    print('Right')
                else:
                    print('NoOp')

            elif loc[current_position] == 0 and current_position == 1:
                decide = random.uniform(0,1)
                if decide < probability:
                    current_position = 0 
                    print('Left')
                else: 
                    print('NoOp')



# ((0, 0), 'Dirty')
# ((1, 0), 'Clean')
# ((1, 0), 'Dirty')
# ((0, 0), 'Clean')