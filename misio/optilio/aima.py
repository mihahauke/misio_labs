from aima3.agents import Agent as _Agent

START_MSG = "START"


def run_agent(agent_creator):
    n_runs, n_steps = [int(x) for x in input().split()]
    for _ in range(n_runs):
        agent = agent_creator()
        for _ in range(n_steps):
            percept = eval(input())
            action = agent.program(percept)
            print(action, flush=True)


def stdin_agent():
    def program(percept):
        print(percept, flush=True)
        return input()

    return _Agent(program)
