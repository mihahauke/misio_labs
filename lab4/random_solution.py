#!/usr/bin/env python3
import numpy as np

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        p_start, p, steps = [x for x in input().split()]
        p_start = np.float64(p_start)
        p = np.float64(p)
        steps = int(steps)
        print("{:0.5f}".format(np.random.random() * steps), flush=True)
