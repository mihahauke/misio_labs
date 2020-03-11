#!/usr/bin/python3

import numpy as np

from misio.uncertain_wumpus.testing import load_world

PRECISION = 2


def azeros(world, p):
    n = len(world)
    m = len(world[1])
    ret = np.zeros((n, m))
    retval = []

    for row in ret:
        retval.append([round(x, PRECISION) for x in row])

    return retval


def print_result(lines, output_file):
    result = "\n".join([" ".join([str(x) for x in line]) for line in lines])
    print(result, file=output_file, flush=True)


if __name__ == "__main__":
    import sys

    input_file = sys.stdin
    output_file = sys.stdout

    instances_num = int(input_file.readline())
    for _ in range(instances_num):
        world, p = load_world(input_file)
        lines = azeros(world, p)
        print_result(lines, output_file)
