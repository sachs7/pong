n = int(input())
def binary(a):
    return int(bin(a)[2:])
for i in range(n):
    a = int(input())
    print(binary(a))
