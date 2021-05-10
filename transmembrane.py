#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa


#Dictionary of aa and their KD scores
KDScores = {"I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8, "G": -0.4,
            "T": -0.7, "S": -0.8, "W": -0.9, "Y": -1.3, "P": -1.6, "H": -3.2, "E": -3.5, 
            "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5}

# Calcualtes the Kyte-Dolittle Score 
def CalculateKD(Sequence):
    score = 0
    for char in Sequence:      # Adds the KD values of each aa in the string Sequence
        score += KDScores[char]
    return score/len(Sequence) # returns the average score


# Checks of the signal peptide and hydrophobic region conditions are met
# Returns a list of the IDs of proteins that satisfy the conditions
def Transmembrane(Sequences):
    TransmembraneID = [] # List to contain the IDs of transmembrane proteins
    
    # loops through each peptide in the Sequences dictionary
    for ID in Sequences:
        SPSegment   = Sequences[ID][:30] # Splits the sequence into the first 30 aa to check for signal peptide
        HSegment    = Sequences[ID][30:] # Splits the sequence into everything after the first 30 aa to check for hydrophobic regions
        SP          = False # Variable to check if the single peptide condition is met
        Hydrophobic = False # Variable to check if hydrophobic region condition is met
        
        # Loops through each 8-mer in the first 30 aa
        for i in range(len(SPSegment) - 8 + 1):
            # Calculates the KD of each 8-mer and sets SP to true if there is a KD > 2.5
            SP_KD   = CalculateKD(SPSegment[i:i+8])
            if SP_KD > 2.5:
                SP  = True
                break
                
        # Loops through each 11-mer in everything after the first 30 aa
        for j in range(len(HSegment) - 11 + 1):
            currSequence        = HSegment[j:j+11]
            if "P" not in currSequence:   # Only calculates the KD of the 11-mer if there is no Proline in the region
                # Calculates the KD of each 11-mer and sets Hydrophobic to true if there is a KD > 2.0
                H_KD            = CalculateKD(currSequence)
                if H_KD > 2.0:
                    Hydrophobic = True
                    break
                    
        # if both conditions are satisified for this protein, append it to the Transmember ID list
        if SP and Hydrophobic:
            TransmembraneID.append(ID)
    return TransmembraneID # return the Transmember ID list


if __name__ == '__main__':
    
    # Opens the file and adds each line to a list Lines
    with open(sys.argv[1]) as f:
        Lines = f.read().splitlines()
    
    Sequences = {} # Dictionary to hold the ID and sequence pairs
    
    # Sets the current Sequence to the first ID in the database
    firstLine    = Lines[0]
    firstSplit   = firstLine.split(" | ")
    currSequence = firstSplit[0][1:]
    sequence     = ""
   
    # loops through every line in the database
    for i in range(1, len(Lines)):
        Line = Lines[i]
        if Line.startswith(">"): # when a header line is reached
            # add the sequence to the currSequence
            Sequences[currSequence] = sequence[:len(sequence) - 1]
            sequence                = ""                # reset the sequence string
            split                   = Line.split(" | ") # update the currSequence variable
            currSequence            = split[0][1:]
        else:
            # if the current line is not a header line, add that line to the sequence string
            sequence += Line
    # add the last ID sequence pair to the dictionary
    Sequences[currSequence] = sequence[:len(sequence) - 1]
    
    
    # Calls the Transmembrane function with the database dictionary
    TransmembraneID = Transmembrane(Sequences)
    # prints the list of the IDs of transmember proteins
    print(TransmembraneID)
    
"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""

"""
#From Lecture
def kd(seq): #this defines hydrophobicity/kd
	return 1.0
#input hydrophobicity values to each amino acid letter, then make function that adds and average it


#get all sequences and print the identifier/name of file
ids = []
proteins = []
with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			words = line.split()
			s = words[0]
			ids.append(s[1:])
			if len(seq) > 0: proteins.append(''.join(seq))
			seq = []
		else: 
			seq.append(line)
	proteins.append(''.join(seq))
print(len(ids), len(proteins))			# this only prints how many IDs and proteins


#look for signal peptides in all sequences
			
			
#look for hydrophobic regions in all sequences
w = 11

for id,seq in zip(ids, proteins):
	print(id, len(seq))
	for i in range(len(seq) - w + 1):
		print(i, kd(seq[i:i+w]))
"""