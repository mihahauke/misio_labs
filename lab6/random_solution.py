#!/usr/bin/env python3

from misio.pacman.agents import RandomAgent
from misio.optilio.pacman import StdIOPacmanRunner

if __name__ == "__main__":
    runner = StdIOPacmanRunner()
    games_num = int(input())

    agent = RandomAgent()
    for _ in range(games_num):
        runner.run_game(agent)
