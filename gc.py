#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

GC = 0
for i in range(len(dna)):
	if dna[i] == "C" or dna[i] == "G":
		GC += 1
print(f'{GC/len(dna):.2f}')
print('{:.2f}'.format(GC/len(dna)))
print('%.2f' % (GC/len(dna)))

"""
python3 gc.py
0.42
0.42
0.42
"""
