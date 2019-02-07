from aima3.agents import Agent as _Agent
from ..aima.testing import DEFAULT_STEPS, DEFAULT_TEST_RUNS
import sys


def run_agent(agent_creator, n=DEFAULT_TEST_RUNS, steps=DEFAULT_STEPS):
    for _ in range(n):
        agent = agent_creator()
        for _ in range(steps):
            percept = eval(input())
            action = agent.program(percept)
            print(action, flush=True)


def std_agent():
    def program(percept):
        print(percept, flush=True)
        return input()

    return _Agent(program)
