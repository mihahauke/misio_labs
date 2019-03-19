import numpy as np
from ._wumpus import Action


class AgentStub(object):
    def __init__(self, map: np.ndarray, p: float, pj: float, pn: float):
        self.p = p
        self.pj = pj
        self.pn = pn
        self.h, self.w = map.shape
        self.map = map.astype(np.float64)

    def sense(self, sensory_input: bool):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def reset(self):
        pass

    def get_histogram(self):
        raise NotImplementedError()


class RandomAgent(AgentStub):
    def __init__(self, *args, **kwargs):
        super(RandomAgent, self).__init__(*args, **kwargs)
        self.histogram = np.ones_like(self.map)

    def sense(self, sensory_input: bool):
        pass

    def move(self):
        return np.random.choice(Action)

    def get_histogram(self):
        return self.histogram


class SnakeAgent(AgentStub):
    def __init__(self, *args, **kwargs):
        super(SnakeAgent, self).__init__(*args, **kwargs)
        self.histogram = np.ones_like(self.map)

        self.times_moved = 0
        self.direction = Action.LEFT

    def sense(self, sensory_input: bool):
        pass

    def move(self):
        if self.times_moved < self.w - 1:
            self.times_moved += 1
            return self.direction
        else:
            self.times_moved = 0
            self.direction = Action.RIGHT if self.direction == Action.LEFT else Action.LEFT
            return Action.DOWN

    def get_histogram(self):
        return self.histogram
