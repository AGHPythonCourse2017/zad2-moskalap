#!/bin/bash

for name in matrix_transpo heapsort bublesort binarysearch list_insertion insertionsort quicksort sorted
do
rm plot.png
python3 playground.py './sample_codes/i_'$name'.py' './sample_codes/x_'$name'.py'
cp plot.png $name.png
done
