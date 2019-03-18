from ._wumpus import Field
import numpy as np


def generate_map(h: int, w: int, cave_density: float):
    assert cave_density > 0
    assert cave_density < 1
    map = np.zeros((h, w), dtype=np.uint8) + Field.EMPTY

    num_caves = int(h * w * cave_density)
    cave_x = np.random.choice(w, size=num_caves, replace=False)
    cave_y = np.random.choice(h, size=num_caves, replace=False)
    map[cave_y, cave_x] = Field.CAVE

    exit_x = np.random.randint(w)
    exit_y = np.random.randint(h)
    map[exit_y, exit_x] = Field.EXIT
    return map, (exit_y, exit_x)


def load_input_file(filename: str, new_format: bool = False):
    with open(filename, "r") as file:
        num_worlds = int(file.readline())
        worlds = []
        if new_format:
            mapping = {x: int(x) for x in range(2)}
        else:
            mapping = {"J": Field.CAVE, "W": Field.EXIT, ".": Field.EMPTY}
        for i in range(num_worlds):
            p = float(file.readline())
            pj, pn = [float(x) for x in file.readline().split()]
            h, w = [int(x) for x in file.readline().split()]

            world = np.zeros((h, w), dtype=np.uint8)
            for i in enumerate(range(h)):
                line = file.readline()
                world[i, :] = [mapping[x] for x in line.strip()]
            worlds.append((world, p, pj, pn))

    return worlds


def load_world_from_stdin(new_format: bool = False):
    import sys
    p = float(input())
    pj, pn = [float(x) for x in input().split()]
    h, w = [int(x) for x in input().split()]
    if new_format:
        mapping = {x: int(x) for x in range(2)}
    else:
        mapping = {"J": Field.CAVE, "W": Field.EXIT, ".": Field.EMPTY}

    world = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        line = input()
        world[i, :] = [mapping[x] for x in line.strip()]

    return world, p, pj, pn


def save_world(
        filename: str, map: np.ndarray,
        p: float,
        pj: float, pn: float,
        new_format: bool = False):

    with open(filename, "w") as file:
        print(p, file=file)
        print(pj, pn, file=file)
        print(*map.shape, file=file)
        if new_format:
            mapping = {x: str(x) for x in range(2)}
        else:
            mapping = {Field.CAVE: "J", Field.EXIT: "W", Field.EMPTY: "."}
        for row in map:
            print("".join([mapping[x] for x in row]), file=file)
