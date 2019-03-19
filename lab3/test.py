#!/usr/bin/env python3

from misio.lost_wumpus.testing import test_locally
from misio.lost_wumpus.agents import RandomAgent
import numpy as np

np.set_printoptions(precision=3, suppress=True)
n = 10

test_locally("tests/2015.in", RandomAgent, n=n)
test_locally("tests/2016.in", RandomAgent, n=n)
