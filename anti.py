#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

rcdna = ''

for i in range(len(dna) -1, -1, -1):
	nt = dna[i]
	if   nt == 'A': nt = 'T'
	elif nt == 'T': nt = 'A'
	elif nt == 'C': nt = 'G'
	elif nt == 'G': nt = 'C'
	else          : nt = 'N'
	rcdna += nt 
print(rcdna)

# for nt in dna[::-1]: print(nt)    <-- reverse order
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
