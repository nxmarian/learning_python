import argparse
import mcb185
import statistics
#from statistics import mean, median
#	so you dont have to type the whole 'statistics.mean'
#	lets u import specific things

parser = argparse.ArgumentParser(description='Stats about sequence')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='fasta file')
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
	#print(name, len(seq))
	length.append(len(seq))
length.sort()
#print(length)

#Min
print('Min is', min(length)) #length[0]

#Max
print('Max is', max(length)) #length[-1]

#sum = 0
#for value in length:
#	sum += value
print('Sum is', sum(length))

#Mean
print('Mean is', statistics.mean(length))

#Median
print('Median is', statistics.median(length))

#N-50 : sum value, once it is greater than 1/2 the sum, break
print('N50 is', mcb185.n50(length))

