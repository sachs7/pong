# Write a function that takes an input string and returns the first non-repeated char in the string. 
# For e.g. if the string is "communication", the function should return 'u'. 
def non_repeated(a):
    maps = {}
    a = str(a)
    if len(str(a)) >= 1: 
      for i in a:
           maps[i] = maps.get(i, 0) + 1
        
      result = []   
      for k, v in maps.items():
          if v ==1:
              result.append(a.index(k) )
      if len(result) == 0:
          return None         
      return a[min(result)]
    else:
      return None
 
print(non_repeated("communication"))  
print(non_repeated("sachin"))  
print(non_repeated("aabbccdd")) 
print(non_repeated(123))
print(non_repeated("aabbccddeeffgghhijjkkllmmnn"))
print(non_repeated(""))
print(non_repeated("  "))
'''
str = ' '
 
str = 12345

sstr = '''