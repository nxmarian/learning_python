#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome = []
gen_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_length = int(sys.argv[3])

for i in range(gen_size):
	genome.append(0)
#print(genome)

for i in range(read_num):
	n = random.randint(0, len(genome) - read_length)
	for j in range(read_length):
		genome[n+j] += 1
#print(genome)

#Min, Max, avg coverage
min = genome[read_length]
max = genome[read_length]
total = 0

for x in genome[read_length: -read_length]:
	if x < min: min = x
	if x > max: max = x
	total += x
	
print(min, max, total/(gen_size - 2*read_length))
"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
