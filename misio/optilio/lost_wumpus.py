from ..lost_wumpus.util import load_input_file
from ..lost_wumpus import Field


def run_agent(agent_class, filename):
    worlds = load_input_file(filename)

    n = int(input())
    for world_i, (m, p, pj, pn) in enumerate(worlds):
        agent = agent_class(m, p, pj, pn)
        for run_i in range(n):
            agent.reset()
            while True:
                state = int(input())
                if state == Field.EXIT:
                    break
                agent.sense(state)
                move = agent.move()
                print(move.value)
