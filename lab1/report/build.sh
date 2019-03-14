#!/usr/bin/env bash

infile="aima_sample_report.tex"
pdflatex ${infile} && pdflatex ${infile}

rm *log *aux