import sys


K,N = input().strip().split(' ')
K,N = [int(K),int(N)]
R = [int(R_temp)**2 for R_temp in input().strip().split(' ')][::-1]
x = []
for x_i in range(N):
   x_t = [int(x_temp) for x_temp in input().strip().split(' ')]
   x.append(x_t)
result = []
score = [i for i in range(1, K+1)][::-1]
for i in range(0, N):
    c, d = x[i]
    a, b = c**2, d**2
    if (a + b) < R[0]:
        result.append(K)
    for j in range(len(R)):
        if (a + b) == R[j]:
            result.append(score[j])
        elif (a + b) > R[-1]:
            result.append(0)
        elif R[j] < (a + b) < R[j+1]:
            result.append(score[j+1])

#print(result)
print(sum(result))

Solution:   python Hackerrank_WoC_2.py
            5 6
            10 8 6 4 2
            0 0
            1 1
            2 2
            3 3
            4 4
            5 5
            
            22   ----> This is the answer
