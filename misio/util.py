import numpy as _np


def generate_deterministic_seeds(seed, n):
    r = _np.random.RandomState(seed=seed)
    seeds = r.randint(0, _np.iinfo(_np.uint32).max, n)
    return seeds
