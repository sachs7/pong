#!/bin/python3

import sys

n = int(input().strip())
s = " "
count = n-1
for i in range(1, n+1):
    print(s*count + i*"#")
    count -= 1
