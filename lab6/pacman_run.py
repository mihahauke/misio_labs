#!/usr/bin/env python3

import numpy as np
import random
import tqdm
from misio.util import generate_deterministic_seeds


def load_agent(full_agent_class_name):
    import importlib
    modulename, agent_class_name = full_agent_class_name.rsplit(".", 1)
    module = importlib.import_module(modulename)
    return getattr(module, agent_class_name)


def parse_args():
    from argparse import ArgumentParser
    from argparse import ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="Pacman runner program.", formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("-n", "--num-games", type=int, default=1,
                        metavar="NUM_GAMES",
                        help="the number of GAMES to play")
    parser.add_argument("-l", "--layout", metavar="LAYOUT_FILE",        default="pacman_layouts/mediumClassic.lay",
                        help="the LAYOUT_FILE from which to load the map layout (see pacman_layouts directory)"
                        )
    parser.add_argument("-a", "--agent",
                        metavar="CLASS", default="misio.pacman.keyboardAgents.KeyboardAgent",
                        help="the agent CLASS to use (full path)",
                        )
    parser.add_argument("-ng", "--no_graphics", action="store_true",
                        help="Generate no graphics output.", default=False)
    parser.add_argument("-sg", "--smart-ghosts",
                        action="store_true", default=False,
                        help="Use malicious ghosts rather random ones.")
    parser.add_argument("-z", "--zoom", type=float, dest="zoom", default=1.0,
                        help="Zoom the size of the graphics window.")
    parser.add_argument("-f", "--frame-time", type=float, default=0.1,
                        help="Time to delay between frames; <0 means keyboard", )
    parser.add_argument("-s", "--seed", help="Random seed.", type=np.uint32,
                        default=None)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-sh", "--show_histogram", action="store_true",
                        help="shows a histogram of scores")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    # Fix the random seed

    if args.seed is not None:
        seeds = generate_deterministic_seeds(args.seed, args.num_games)
    else:
        seeds = None
    # Choose a Pacman agent
    AgentClass = load_agent(args.agent)
    agent = AgentClass()
    from misio.pacman.pacman import LocalPacmanGameRunner

    runner = LocalPacmanGameRunner(layout_dir=args.layout,
                                   random_ghosts=not args.smart_ghosts,
                                   show_window=not args.no_graphics,
                                   zoom_window=args.zoom,
                                   frame_time=args.frame_time)

    games = []
    for i in tqdm.trange(args.num_games, leave=False):
        if seeds is not None:
            random.seed(seeds[i])
        game = runner.run_game(agent)
        games.append(game)
    scores = [game.state.getScore() for game in games]
    results = np.array([game.state.isWin() for game in games])
    print("Avg score:     {:0.2f}".format(np.mean(scores)))
    print("Best score:    {:0.2f}".format(max(scores)))
    print("Median score:  {:0.2f}".format(np.median(scores)))
    print("Worst score:   {:0.2f}".format(min(scores)))
    print("Win Rate:      {}/{} {:0.2f}".format(results.sum(), len(results), results.mean()))

    if args.show_histogram:
        from matplotlib import pyplot as plt
        plt.hist(scores)
        plt.show()
