#!usr/bin/python3
from aima3.agents import *
from misio.aima import * 

current_position = random.choice([0,1])
loc = [0, 0]
iter = 0
ac = 0
flag = False

def MyAgent(): 
    def program(percept): 
        location, status = percept 
        global current_position 
        global loc 
        global iter
        global ac
        global flag 

        loc[location[0]] = (1 if status == 'Dirty' else 0) # status

        if loc[current_position] == 1:
            loc[current_position] = 0
            flag = True
            return 'Suck'

        elif (ac == 0) or (ac == 1 and flag):
            if current_position == 0: return 'Left'
            else: return 'Right'

        elif sum(loc) == 0 and iter < 8: 
            return 'NoOp'

        elif loc[current_position] == 0 and current_position == 0:
            iter = 0
            current_position = 1
            return 'Right'

        elif loc[current_position] == 0 and current_position == 1:
            iter = 0
            current_position = 0 
            return 'Left'

        iter += 1
        ac += 1 
    
    return Agent(program)

MyAgent()