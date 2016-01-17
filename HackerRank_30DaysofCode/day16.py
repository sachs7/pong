import sys
n = int(input())
val = sorted(list(map(int, input().split())))
minimum = sys.maxsize;
for i in range(n-1):
    if abs(val[i+1]-val[i]) < minimum:
        result = str(val[i]) + " " + str(val[i+1])
        minimum = abs(val[i+1]-val[i])
    elif abs(val[i+1]-val[i]) == minimum:
        result += " " + str(val[i]) + " " + str(val[i+1])
print(result)        



OR


n = int(input())
val = sorted(list(map(int, input().split())))
minimum = max(val)
d = {}
for i in range(1, n):
    if abs(val[i] - val[i-1]) < minimum:
        minimum = abs(val[i] - val[i-1])
        if minimum in d:
            d[minimum].append(val[i-1])
            d[minimum].append(val[i])
        else:
            d[minimum] = [val[i-1]]
            d[minimum].append(val[i])
ans = min(d)
for i in d[ans]:
    print(i, end= " ")
