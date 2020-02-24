#!/usr/bin/env python3

import argparse

from misio.util import generate_deterministic_seeds

from tqdm import trange
import gym
import numpy as np
import random
import time

random_state = np.random.RandomState(123)

if __name__ == "__main__":

    # env = gym.make('BipedalWalker-v2')

    n_games = 100
    seed = 123
    seeds = generate_deterministic_seeds(seed, n_games)


    env = gym.make("Pendulum-v0")
    # env = gym.make("BipedalWalker-v2")
    rewards = []
    for i_episode in trange(n_games):
        np.random.seed(seeds[i_episode])
        random.seed(seeds[i_episode])
        env.seed(int(seeds[i_episode]))
        state = env.reset()
        done = False
        total_reward = 0
        while not done:
            # env.render()
            # time.sleep(0.05)
            action = (random_state.rand(env.action_space.shape[0])-0.5)*2*env.action_space.high
            new_state, reward, done, info = env.step(action  )
            total_reward += reward
            if done:
                break
        print(total_reward)
        rewards.append(total_reward)
    print("Avg reward: {:0.2f}".format(np.mean(rewards)))
    print("Min reward: {:0.2f}".format(np.min(rewards)))
    print("Max reward: {:0.2f}".format(np.max(rewards)))
    print()
env.close()
