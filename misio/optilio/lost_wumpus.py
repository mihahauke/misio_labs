from ..lost_wumpus.util import load_world_from_stdin
from ..lost_wumpus import Field


def run_agent(agent_class):
    n_worlds = int(input())
    n_runs = int(input())
    for world_i in range(n_worlds):
        m, p, pj, pn = load_world_from_stdin()
        agent = agent_class(m, p, pj, pn)
        for run_i in range(n_runs):
            agent.reset()
            while True:
                state = int(input())
                if state == Field.EXIT:
                    break
                agent.sense(state)
                move = agent.move()
                print(move.value)
