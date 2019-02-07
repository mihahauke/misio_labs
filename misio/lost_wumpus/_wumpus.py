import numpy as np
from enum import Enum


class World():
    """Znaki z ktorych sklada sie mapa swiata."""

    EXIT = 2
    """Znak umieszczany mapie oznaczajacy pole z wyjsciem."""

    CAVE = 1
    """Znak umieszczany mapie oznaczajacy pole z jama."""

    EMPTY = 0
    """Znak umieszczany mapie oznaczajacy puste pole."""


class Action(Enum):
    UP = '-Y'
    """Ruch w gore (w kierunku malejacych indeksow Y)."""

    DOWN = '+Y'
    """Ruch w dol (w kierunku rosnacych indeksow Y)."""

    LEFT = '-X'
    """Ruch w lewo (w kierunku malejacych indeksow X)."""

    RIGHT = '+X'
    """Ruch w prawo (w kierunku rosnacych indeksow X)."""


class LostWumpusGame(object):
    def __init__(self, map: np.ndarray, p: float, pj: float, pn: float, exit_loc: tuple = None, max_moves=None):
        assert isinstance(map, np.ndarray)
        self.map = map
        self.h, self.w = map.shape
        self.p = p
        self.pj = pj
        self.pn = pn
        if exit_loc is None:
            exit_loc = [int(x) for x in np.where(map == World.EXIT)]
        self.exit_loc = list(exit_loc)
        self.position = list(exit_loc)
        self.moves = np.inf
        self.finished = True
        self.sensory_output = None
        # TODO Compute some reasonable limit based on n and m
        if max_moves is None:
            max_moves = np.inf
        self.max_moves = max_moves

    def reset(self):
        self.moves = 0
        self.finished = False
        self.position=self.exit_loc
        while self.position == self.exit_loc:
            self.position = [np.random.randint(self.h), np.random.randint(self.w)]
        self._update_sensory_output()

    def apply_move(self, action: Action):
        assert not self.finished
        assert isinstance(action, Action)
        motion = [0, 0]
        if action == Action.LEFT:
            motion[1] -= 1
        elif action == Action.RIGHT:
            motion[1] += 1
        elif action == Action.UP:
            motion[0] -= 1
        elif action == Action.DOWN:
            motion[0] += 1

        if np.random.random() > self.p:
            motion[np.random.randint(2)] += np.random.choice([-1, 1])
        self.position[0] += motion[0]
        self.position[1] += motion[1]
        self.position[0] %= self.h
        self.position[1] %= self.w

        self.moves += 1
        self._update_sensory_output()

        if self.position == self.exit_loc or self.moves >= self.max_moves:
            self.finished = True
            self.sensory_output = None

    def _update_sensory_output(self):
        if self.map[self.position[0], self.position[1]] == World.CAVE:
            self.sensory_output = np.random.binomial(1, self.pj)
        else:
            self.sensory_output = np.random.binomial(1, self.pn)


def generate_map(h: int, w: int, cave_density: float):
    assert cave_density > 0
    assert cave_density < 1
    map = np.zeros((h, w), dtype=np.uint8) + World.EMPTY

    num_caves = int(h * w * cave_density)
    cave_x = np.random.choice(w, size=num_caves, replace=False)
    cave_y = np.random.choice(h, size=num_caves, replace=False)
    map[cave_y, cave_x] = World.CAVE

    exit_x = np.random.randint(w)
    exit_y = np.random.randint(h)
    map[exit_y, exit_x] = World.EXIT
    return map, (exit_y, exit_x)


def load_world(filename: str, new_format: bool = False):
    with open(filename, "r") as file:
        p = float(file.readline())
        pj, pn = [float(x) for x in file.readline().split()]
        h, w = [int(x) for x in file.readline().split()]
        if new_format:
            mapping = {x: int(x) for x in range(2)}
        else:
            mapping = {"J": World.CAVE, "W": World.EXIT, ".": World.EMPTY}

        map = np.zeros((h, w), dtype=np.uint8)
        for i in enumerate(range(h)):
            line=file.readline()
            line = [mapping[x] for x in line.strip()]
            map[i, :] = line

    return map, p, pj, pn


def save_world(
        filename: str, map: np.ndarray,
        p: float,
        pj: float, pn: float,
        new_format: bool = False):
    with open(filename, "w") as file:
        print(p, file=file)
        print(pj, pn, file=file)
        print(*map.shape, file=file)
        if new_format:
            mapping = {x: str(x) for x in range(2)}
        else:
            mapping = {World.CAVE: "J", World.EXIT: "W", World.EMPTY: "."}
        for row in map:
            print("".join([mapping[x] for x in row]), file=file)


class AgentStub(object):
    def __init__(self, map, p, pj, pn):
        pass

    def sense(self, sensory_input: bool):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def reset(self):
        pass

    def get_histogram(self):
        raise NotImplementedError()


class RandomAgentStub(AgentStub):
    def __init__self(self, map, p, pj, pn):
        self.histogram = np.ones_like(map)

    def sense(self, sensory_input: bool):
        pass

    def move(self):
        return np.random.choice(Action)

    def get_histogram(self):
        return self.histogram