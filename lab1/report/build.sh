#!/usr/bin/env bash

infile="lab1_125342.tex"
pdflatex ${infile} && pdflatex ${infile}

rm *log *out *aux