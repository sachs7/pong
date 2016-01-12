T = int(input())
for i in range(T):
    a, b, N = list(map(int, input().split()))
    suming = 0
    temp = a + (2**0 * b)
    suming += temp
    print(suming, end=" ")
    for j in range(1, N):
        suming += (2 ** j * b) 
        print(suming, end=" ")
    print("")
