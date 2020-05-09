#!/usr/bin/env bash

# downloads pacman layouts:
if [[ ! -d "pacman_layouts" ]]
then
    git clone https://github.com/mihahauke/misio_labs
    mv misio_labs/lab6/pacman_layouts .
    rm -rf misio_labs
fi

./my_random_solution.py --train