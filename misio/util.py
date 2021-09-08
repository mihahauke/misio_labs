import numpy as _np


def generate_deterministic_seeds(seed, shape, res_type=_np.uint32):
    r = _np.random.RandomState(seed=seed)
    seeds = r.randint(0, _np.iinfo(res_type).max, shape)
    return seeds
