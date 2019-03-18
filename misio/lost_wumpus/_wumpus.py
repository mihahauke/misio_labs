import numpy as np
from enum import Enum, IntEnum


class Field(IntEnum):
    """Znaki z ktorych sklada sie mapa swiata."""

    EXIT = 2
    """Znak umieszczany mapie oznaczajacy pole z wyjsciem."""

    CAVE = 1
    """Znak umieszczany mapie oznaczajacy pole z jama."""

    EMPTY = 0
    """Znak umieszczany mapie oznaczajacy puste pole."""


class Action(Enum):
    UP = 'UP'
    """Ruch w gore (w kierunku malejacych indeksow Y)."""

    DOWN = 'DOWN'
    """Ruch w dol (w kierunku rosnacych indeksow Y)."""

    LEFT = 'LEFT'
    """Ruch w lewo (w kierunku malejacych indeksow X)."""

    RIGHT = 'RIGHT'
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
            exit_loc = [int(x) for x in np.where(map == Field.EXIT)]
        self.exit_loc = list(exit_loc)
        self.position = list(exit_loc)
        self.moves = np.inf
        self.finished = True
        self.sensory_output = None
        if max_moves is None:
            max_moves = np.inf
        self.max_moves = max_moves

    def reset(self):
        self.moves = 0
        self.finished = False
        self.position = self.exit_loc
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
        if self.map[self.position[0], self.position[1]] == Field.CAVE:
            self.sensory_output = np.random.binomial(1, self.pj)
        else:
            self.sensory_output = np.random.binomial(1, self.pn)

