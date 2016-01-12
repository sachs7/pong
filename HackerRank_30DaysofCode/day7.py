#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
res = arr[::-1]
for i in res:
    print(i, end=" ")
