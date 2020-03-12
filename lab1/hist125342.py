#!usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
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


no_samples = 100000
n = 1
steps = 50
confidence = .95

def agent_factory_1():
    return MyAgent()

def env_factory():
    return TrivialVacuumEnvironmentWithChildren(random_dirt_prob=0.05)

def run_agent(EnvFactory, AgentFactory, n=10, steps=1000):
    envs = [EnvFactory() for i in range(n)]
    return test_agent(AgentFactory, steps, copy.deepcopy(envs))

data = [run_agent(env_factory, agent_factory_1, n, steps) for _ in range(no_samples)]

print("Expected val. {}, std. dev. {}.".format(np.mean(data), np.std(data)))
print(st.norm.interval(confidence, loc=np.mean(data), scale=st.sem(data)))

plt.style.use("seaborn-deep")
plt.hist(data, density=True, bins=20)
plt.show()