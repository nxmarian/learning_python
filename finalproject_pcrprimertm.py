import sys
import argparse
import mcb185

# MCB185 Final Project
# Design a program that can evaluate PCR primers Tm 
# Tm = melting temperature
# Good primers recommended to have 18-45 bases, 40-60% GC, Tm around 78C+
# Program should be able to :
	# calculate GC %
	# count number of bases in primer
	# optionally add % mismatch 
	# input this all into equation Tm = 81.5 + 0.41(%GC) - 675/N - % mismatch
	# N = total number of bases
# output should be (name, # of bases, GC %, Tm in C )


# Setup
parser = argparse.ArgumentParser(description='evaluates PCR primer Tm')

# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='put fasta file')

# optional argument
parser.add_argument('--mismatch', required=False, type=float, default=0,
	metavar='<float>', help='mismatch percentage [%(default).3f]')
parser.add_argument('--info', action='store_true',
	help='provide additional info')

# finalization
arg = parser.parse_args()

if arg.info:
	print('Output is name, length of sequence in bases, GC %, Tm in Celsius')
	
	
def gc(seq):
	g = seq.count('G')
	c = seq.count('C')
	return ((g+c)/len(seq)*100) #calculates GC percentage
	

for name, seq in mcb185.read_fasta(arg.fasta):
	Tm = 81.5+(0.41*gc(seq))-(675/len(seq))-arg.mismatch #Tm formula
	
	print(name, len(seq), '{:.2f}%'.format(gc(seq)), '{:.2f}C'.format(Tm))

