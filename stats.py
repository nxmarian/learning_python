#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
stats = []

for i in sys.argv[1:]:
	stats.append(int(i))
print(stats)

#Count
count = len(sys.argv[1:])
for i in stats:
	count += 1
print('Count:', count)

#Finding Min
stats.sort()
for i in stats[1:]:
	if i < min : min = i
print('Minimum', min)

#Finding Max
for i in stats[-1:]:
	if i > max : max = i
print('Maximum:', max)

#Finding Mean
sumx = 0
for i in stats: 
	sumx += i
	mean = sumx/len(sys.argv[1:]) #why does it keep saying division by 0
	print('Mean:', f'{mean:.3f}')

#Finding Standard Deviation
sumy = 0
for i in stats:
	numerator = (i - mean) ** 2
	sumy += numerator
	std_dev = math.sqrt(sumy/count)
	print('Std dev:', std_dev)

#Finding Median
stats.sort()
for i in stats:
	if count % 2 == 0: 
		median = (stats[int((count/2)-1)] + stats[int(count/2)]) / 2
	else: 
		median = stats[int(count/2)]
#median = stats[int(count/2)]
	print('Median:', median)

"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
