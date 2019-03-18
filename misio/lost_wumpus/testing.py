import tqdm
import numpy as np
from ._wumpus import LostWumpusGame, Action
from .util import load_input_file
import traceback
from ..util import generate_deterministic_seeds

DEFAULT_TEST_RUNS = 100


def default_steps_constraint(world):
    return world.shape[0] * world.shape[1] * 2


def test_locally(filename, agent_class,
                 n: int = 100,
                 seed: int = None,
                 verbose: bool = False):
    mean_scores = []
    stds = []

    if seed is not None:
        np.random.seed(seed)
    run_seeds = generate_deterministic_seeds(seed, n)

    worlds = load_input_file(filename)
    for world_i, (m, p, pj, pn) in enumerate(worlds):
        agent = agent_class(m, p, pj, pn)
        max_moves = default_steps_constraint(m)
        game = LostWumpusGame(m, p, pj, pn, max_moves=max_moves)

        run_scores = []
        for run_i in tqdm.trange(n, leave=False, desc="map{}/{}".format(world_i, len(worlds))):
            np.random.seed(run_seeds[run_i])
            agent.reset()
            game.reset()
            while not game.finished:
                move = None
                try:
                    agent.sense(game.sensory_output)
                    move = agent.move()
                except:
                    print("Stop Wumpus. You're drunk. ABORTING.")
                    traceback.print_exc()
                    exit(-1)
                try:
                    if move not in Action:
                        print("Action: '{}' not supported".format(move))
                        exit(-2)
                    game.apply_move(move)
                except:
                    print("Environment failed. Please report it. ABORTING.")
                    traceback.print_exc()
                    exit(-3)
            run_scores.append(game.moves)
        mean_score = np.mean(run_scores)
        std = np.std(run_scores)
        mean_scores.append(mean_score)
        stds.append(std)
        if verbose:
            print("map{}: avg score: {:0.2f} ±{:0.2f}".format(world_i, mean_score, std))

    mean_total_score = np.sum(mean_scores)
    total_std = (np.array(stds) ** 2).sum() ** 0.5
    if verbose:
        print()
    print("Total score: {:0.2f} ± {:0.2f}".format(mean_total_score, total_std))
