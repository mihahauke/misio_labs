from aima3.agents import Environment, loc_A,loc_B,Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent,TableDrivenVacuumAgent, ModelBasedVacuumAgent
import random


class TrivialVacuumEnvironmentWithChildren(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean.  The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self, random_dirt_prob=0.05, seed=None):
        super(TrivialVacuumEnvironmentWithChildren, self).__init__()
        self.random = random.Random(seed)
        self.status = {loc_A: self.random.choice(['Clean', 'Dirty']),
                       loc_B: self.random.choice(['Clean', 'Dirty'])}
        self.random_dirt_prob = random_dirt_prob

    def thing_classes(self):
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent,
                TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        "Returns the agent's location, and the location status (Dirty/Clean)."
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            agent.location = loc_B
            agent.performance -= 1
        elif action == 'Left':
            agent.location = loc_A
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'

        # Children can make either location dirty
        for loc in [loc_A, loc_B]:
            if self.random.random() < self.random_dirt_prob:
                self.status[loc] = 'Dirty'

    def default_location(self, thing):
        "Agents start in either location at random."
        return self.random.choice([loc_A, loc_B])
