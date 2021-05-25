import sys
import mcb185

for name, seq in mcb185.read_fasta(sys.argv[1]):
	print(mcb.translate(seq))
	
	

# You have been given the code above
# An example command line is
#	python3 translate.py ATGCGCCCGAACTAG ATGAAACCCGGGTTT

# Your task is to write a new program with the following features
# 1. Proper command line (argparse)
# 2. Reads sequences in from fasta format rather than sys.argv
# 3. Outputs sequences as fasta format
# 4. Accepts both uppercase and lowercase letters
# 5. Translates ambiguous amino acids as X (e.g. for weird codons)

# Hints
# 1. add functions and put them in your library
# 2. use string.upper() to normalize case
