#!/bin/bash

for name in sleep bublesort binarysearch insertion insertionsort quicksort
do
rm plot.png
python3 playground.py './sample_codes/i_'$name'.py' './sample_codes/x_'$name'.py'
cp plot.png $name.png
done
