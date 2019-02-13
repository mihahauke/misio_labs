import numpy as np


def load_world(infile):
    first_line = infile.readline().split()
    n = int(first_line[0])
    p = float(infile.readline())
    world = []
    for i in range(n):
        world.append(list(infile.readline().strip()))

    return world, p


def test_locally(program,
                 input_filename,
                 baseline_filename):
    from time import time
    import itertools
    def load_float_matrix(file, lines_num):
        lines = [file.readline() for _ in range(lines_num)]
        return [float(x) for x in " ".join(lines).split()]

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
            for world, p in instances:
                user_output = list(itertools.chain.from_iterable(program(world, p)))
                result = (user_output == load_float_matrix(output_file, len(world)))
                results.append(result)
            end_time = time()
            time_delta = end_time - start_time
        except:
            wa = True
            time_delta = np.inf

    if wa:
        print("Output file incorrect.")
    else:
        ok_results = (np.array(results)).sum()
        print("score: {}/{}   time: {:0.3f}s".format(ok_results, len(results), time_delta))
