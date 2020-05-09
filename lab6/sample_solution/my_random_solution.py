#!/usr/bin/env python3

from misio.pacman.agents import RandomAgent
from misio.optilio.pacman import StdIOPacmanRunner

from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--train", action="store_true")
    args, _ = parser.parse_known_args()

    if args.train:
        print("'Training' of the random agent has begun.")
        # Your code here
        with open("weights.txt", "w") as f:
            print("1.0 3.0 3.56456", file=f)
        print("And it's finished.")
    else:
        runner = StdIOPacmanRunner()
        games_num = int(input())

        agent = RandomAgent()
        # 'load' weights
        with open("weights.txt") as f:
            weights = [float(x) for x in f.readline().split()]
        for _ in range(games_num):
            runner.run_game(agent)
