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
 
print(non_repeated("communication"))                  # u
print(non_repeated("sachin"))                         # s
print(non_repeated("aabbccdd"))                       # None
print(non_repeated(123))                              # 1
print(non_repeated("aabbccddeeffgghhijjkkllmmnn"))    # i
print(non_repeated(""))                               # None
print(non_repeated("  "))                             # None
