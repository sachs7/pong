import sys
from fractions import gcd
from itertools import product

a, b, c, d = [4, 4, 4, 4]
count = 0

for i in range(1, a+1):
	for j in range(1, b+1):
		for k in range(1, c+1):
			for x in range(1, d+1):
				if (i-j)%3 == 0 and (j+k)%5 ==0 and (i*k)%4 ==0 and gcd(i, x) == 1:
					count +=1
					# print(i, j, k, x)
				else:
					continue
print(count)

Solution:  python Hackerrank_WoC.py
           
           8   -> Answer
