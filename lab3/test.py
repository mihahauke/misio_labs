#!/usr/bin/env python3

from misio.lost_wumpus.testing import test_locally
from misio.lost_wumpus.agents import RandomAgent
import numpy as np

n = 10

score0 = test_locally("tests/2015.in", RandomAgent, n=n)
score1 = test_locally("tests/2016.in", RandomAgent, n=n)
print("scores: {:0.2f}, {:0.2f}".format(score0, score1))
