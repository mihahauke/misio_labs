#!/usr/bin/env python3

from os import walk

import numpy as np

from lab6.qlearningAgents import PacmanQAgent
from misio.pacman.pacman import LocalPacmanGameRunner

if __name__ == "__main__":
    agent = PacmanQAgent()

    "*** DISABLE TRAINING HERE ***"

    all_results = []
    for (dirpath, dirnames, filenames) in walk("sample_solution/pacman_layouts"):
        for layout in filenames:
            runner = LocalPacmanGameRunner(layout_path=f"{dirpath}/{layout}",
                                           random_ghosts=True,
                                           show_window=False,
                                           timeout=-1000)

            games = []
            for i in range(10):
                game = runner.run_game(agent)
                games.append(game)
            scores = [game.state.getScore() for game in games]
            results = np.array([game.state.isWin() for game in games])

            all_results += list(results)

            print(layout)
            print(f"Avg score:     {np.mean(scores):0.2f}")
            print(f"Best score:    {max(scores):0.2f}")
            print(f"Median score:  {np.median(scores):0.2f}")
            print(f"Worst score:   {min(scores):0.2f}")
            print(f"Win Rate:      {results.sum()}/{len(results)} {results.mean():0.2f}")
            print()

        all_results = np.array(all_results)
        print("Total")
        print(f"Win Rate:      {all_results.sum()}/{len(all_results)} {all_results.mean():0.2f}")
        print()
