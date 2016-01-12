import sys
n = int(input().strip()) 
dict = {} 
for i in range(n): 
    name = input().strip() 
    number = input().strip() 
    dict[name] = number 
for name in sys.stdin: 
    name = name.strip() 
    if name in dict: 
        print(name+"="+dict[name]) 
    else: 
        print("Not found")
