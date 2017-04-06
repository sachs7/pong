def has_unique_chars(s):
  d = {}
  if s == None or type(s) == int or type(s) == float:
    return False
  for i in s:
    d[i] = d.get(i,0) + 1
    if d[i] > 1:
      return False
  return True
  
Example: 

In [37]: has_unique_chars(23.2)
Out[37]: False

In [38]: has_unique_chars(23)
Out[38]: False

In [39]: has_unique_chars(None)
Out[39]: False

In [40]: has_unique_chars('')
Out[40]: True

In [41]: has_unique_chars('foo')
Out[41]: False

In [42]: has_unique_chars('bar')
Out[42]: True

In [43]: has_unique_chars('0')
Out[43]: True

In [44]: has_unique_chars('test')
Out[44]: False
