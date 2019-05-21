#!/usr/bin/env python3

import numpy as np

rstate = np.random.RandomState(123)
if __name__ == "__main__":
    game = input()
    if game =="BipedalWalker-v2":
        action_dimensions = 4
        high = 1
    elif game =="Pendulum-v0":
        action_dimensions = 1
        high = 2
    else:
        raise ValueError("Unexpected game: {}".format(game))
    num_games = int(input())

    for _ in range(num_games):
        while True:
            state = input()
            if state =="END":
                break
            print((rstate.rand(action_dimensions)-0.5)*2*high,flush=True)
