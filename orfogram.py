#!/usr/bin/env python3

import argparse
import mcb185
import random
import statistics

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

#check to see which sequence length is unlikely
#	generate random sequences and gc compositions
#	look for ORF
#	compare how often each ORF length shows up
#	pick the unlikely length 

#Setup
parser = argparse.ArgumentParser(description='Explore ORF Length')
# optional arguments with default parameters
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<str>', help='genome size [%(default)i]')
parser.add_argument('--orfmin', required=False, type=int, default=100,
	metavar='<int>', help='minimum orf length [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='gc fraction [%(default).3f]')
# switches
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
arg = parser.parse_args()	

if arg.seed: #keeps random numbers fixed aka no new random sequences each time it runs
	random.seed(1)
if arg.info: 
	print(arg.size, arg.orfmin, arg.gc)

#Generate random sequence of specified size and gc composition
seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)

#Look for ORF
length = []
for i in range(len(seq) - 2):
	start = None
	stop = None
	if seq[i: i + 3] == 'ATG':
		start = i
		for j in range(i, len(seq) - 2, 3):
			codon = seq[j: j + 3]
			if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
				stop = j
				break
	if stop != None:
		length.sort()
		length.append((stop - start)//3)


count = 0
for n in length:
	if n > arg.orfmin:
		count += 1
print(count)


#Make histogram
histogram = [0] * (max(length) + 1)
for n in length:
	histogram[n] += 1

w = histogram
for x in range(len(w)):
	print('Length', x, 'Count:', histogram[x])


