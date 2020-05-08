#!/usr/bin/python3


import numpy as np
import sys

if __name__ == "__main__":
    instances_num = int(input())
    for _ in range(instances_num):
        max_cars = int(input())
        gamma = float(input())
        _ = [float(x) for x in input().split()]
        _ = float(input())
        _ = float(input())

        to_move = int(input())
        random_policy = np.random.randint(-to_move, to_move, (max_cars + 1, max_cars + 1), dtype=np.int)
        np.savetxt(sys.stdout, random_policy, fmt='%2d')