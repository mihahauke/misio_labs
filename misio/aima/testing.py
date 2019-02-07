from ._env import TrivialVacuumEnvironmentWithChildren as _env
DEFAULT_STEPS = 50
DEFAULT_TEST_RUNS = 5000

def test_locally(agent_creator, steps=DEFAULT_STEPS, n=DEFAULT_TEST_RUNS, seed=None, progress_bar=True):
    from ..util import generate_deterministic_seeds

    seeds = generate_deterministic_seeds(seed, n)

    if progress_bar:

        try:
            import tqdm
            seeds = tqdm.tqdm(seeds, leave=False)
        except ImportError:
            print("Cannot launch progress bar. To enable progress bar please install tqdm: 'sudo pip3 install tqdm'")
    scores = []
    for seed in seeds:
        agent = agent_creator()
        env = _env(random_dirt_prob=0.05, seed=seed)
        env.add_thing(agent)
        env.run(steps)
        scores.append(agent.performance)
    return scores
