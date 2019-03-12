from aima3.agents import Agent as _Agent

START_MSG = "START"


def run_agent(agent_creator):
    n_runs, n_steps = [int(x) for x in input().split()]
    agent = agent_creator()
    for _ in range(n_runs):
        for _ in range(n_steps):
            env_info = input()
            percept = (int(env_info[2]), int(env_info[5])), env_info[10:15]
            action = agent.program(percept)
            print(action, flush=True)


def stdin_agent():
    def program(percept):
        print(percept, flush=True)
        return input()

    return _Agent(program)
