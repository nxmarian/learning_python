import sys
import random
import statistics

def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#Counts GC fraction
def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g+c)/len(dna)
	
#Calculates N-50
def n50(length):
	length.sort()
	running_sum = 0
	total = sum(length)
	for value in length:
		running_sum += value
		if running_sum > total/2:
			return value
			
#def n50(length):
#	length.sort()
#	running_sum = 0
#	total = sum(length)
#	i = 0
#	while running_sum < total/2:
#		running_sum += length[i]
#		i += 1
#	return length[i]

#Create random sequence of specified length and gc composition
#	seq = mcb185.randseq(arg.size, arg.gc)
def randseq(length, gc):
	seq = ''
	for i in range(length):
		if random.random() < gc:
			seq += random.choice('GC')
		else:
			seq += random.choice('AT')
	return seq
	
	
#Look for ORF length
def orflen(seq):
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
	return lengths


#Look for ORF
def orfseq(seq):
	orfseq = []
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
			orfseq.append(seq[start:stop])
	return orfseq


#Sort ORF to get longest one including reverse
def maxorf(seq):
	maxorf = []
	for name, seq in mcb185.read_fasta(arg.file):
		seq = mcb185.orfseq(seq)
		reverse_seq = mcb185.orfseq(reverse)
		seq += reverse_seq
		seq.sort(key=len, reverse=True)
		maxorf = seq[0]
	


#translate dictionary
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

#translate
def translate(seq):
	seq = seq.upper()
	protein = ''
	for i in range(0, len(seq) -2, 3):
		codon = seq [i:i+3]
		if codon in gcode:
			protein += gcode[codon]
		else:
			protein += 'X'
	return protein


#reverse complement
def reverse(seq):
	dna = ''
	for n in range(len(seq)-1, -1, -1):
		if   n == 'A': dna += 'T'
		elif n == 'C': dna += 'G'
		elif n == 'G': dna += 'C'
		elif n == 'T': dna += 'A'
		else:
			dna += 'X'
	return dna
			





