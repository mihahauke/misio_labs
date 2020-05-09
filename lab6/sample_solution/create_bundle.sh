#!/usr/bin/env bash

main_file="my_random_solution.py"
archive="${main_file}".tgz

tar -cvzf ${archive} ${main_file} weights.txt dummy_file.py instruction.md train.sh