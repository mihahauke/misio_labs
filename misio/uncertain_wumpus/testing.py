import numpy as np

POINTS_FOR_TEST = 15.0


def load_world(infile):
    first_line = infile.readline().split()
    n = int(first_line[0])
    p = np.float64(infile.readline())
    world = []
    for i in range(n):
        world.append(list(infile.readline().strip()))

    return world, p


def compare_outputs(w0, w1):
    return abs((np.array(w0, dtype=np.float64) - np.array(w1, dtype=np.float64))).mean() < 0.0005


def load_output(file, lines_num):
    lines = [file.readline() for _ in range(lines_num)]
    lines = [np.float64(x) for x in " ".join(lines).split()]
    return lines


def test_locally(program,
                 input_filename,
                 baseline_filename):
    from time import time
    import itertools
    import tqdm

    results = []
    wa = False
    with open(input_filename) as input_file, \
            open(baseline_filename) as output_file:

        num_instances = int(input_file.readline())
        instances = []
        for _ in range(num_instances):
            world, p = load_world(input_file)
            instances.append([world, p])
        try:
            start_time = time()
            for world, p in tqdm.tqdm(instances, leave=False):
                user_output = list(itertools.chain.from_iterable(program(world, p)))
                correct_output = load_output(output_file, len(world))
                result = compare_outputs(user_output, correct_output)
                results.append(result)
            end_time = time()
            time_delta = end_time - start_time
        except:
            wa = True
            time_delta = np.inf

    if wa:
        import sys
        print("Output file incorrect.", file=sys.stderr)
    else:
        return results, time_delta
