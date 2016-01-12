def find_gcd(a,b):
   #Write base condition
    if a % b == 0:
        return b
    return find_gcd(b,a%b)
#Take input
a, b = list(map(int, input().split()))
gcd=find_gcd(a,b)
print (gcd)
