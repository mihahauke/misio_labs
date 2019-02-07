import tqdm
import numpy as np
from ._wumpus import load_world, LostWumpusGame
import traceback


def test_locally(filenames_or_dir, agent_class,
                 n: int = 100,
                 seed: int = None,
                 verbose: bool = False,
                 max_moves=None):
    if isinstance(filenames_or_dir, list):
        filenames = filenames_or_dir
    else:
        import glob
        filenames = sorted(glob.glob(filenames_or_dir + "/*"))
    mean_scores = []
    stds = []

    if seed is not None:
        np.random.seed(seed)
    run_seeds = np.random.randint(0, np.iinfo(np.uint32).max, n)

    for filename in filenames:
        m, p, pj, pn = load_world(filename)
        agent = agent_class(m, p, pj, pn)
        if max_moves is None:
            max_moves = np.product(m.shape) * 2
        game = LostWumpusGame(m, p, pj, pn, max_moves=max_moves)
        filename_short = filename.split("/")[-1]

        run_scores = []
        for run_i in tqdm.trange(n, leave=False, desc=filename_short):
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
                    game.apply_move(move)
                except:
                    print("Environment failed. Pleaser report it. ABORTING.")
                    traceback.print_exc()
                    exit(-2)

            run_scores.append(game.moves)
        mean_score = np.mean(run_scores)
        std = np.std(run_scores)
        mean_scores.append(mean_score)
        stds.append(std)
        if verbose:
            print("{}: avg score: {:0.2f} ±{:0.2f}".format(filename_short, mean_score, std))
    mean_total_score = np.sum(mean_scores)
    total_std = (np.array(stds) ** 2).sum() ** 0.5
    if verbose:
        print()
    print("Total score: {:0.2f} ± {:0.2f}".format(mean_total_score, total_std))
