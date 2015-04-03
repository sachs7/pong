def cycle(seq):
	res = [] # Holds the result
	indx = 0
	
	""" Loop through all the elements of the list """
	
	for i in range(len(seq)):
	
		""" Check if the first element is in remaining items of array/list, if it then append the item and its index in the 'res' """
		if seq[i] in seq[(i + 1):]:
			res.append([seq[i], seq.index(seq[i])])
			""" Get the first elements index """
			indx = res[0][1]
		else:
			continue
			
	""" Get only the unique elements from the 'res' """		
	unik = set(map(tuple,res))
	lenght = len(unik)
	
	""" If no elements are repeated in the given sequence then return empty list """
	if indx == 0 and lenght == 0:
		return []
		
	return ([indx, lenght])
	
	
print(cycle([2, 0, 6, 3, 1, 6, 3, 1, 6, 3, 1]))	

Sample Output:
  [2,3] Since in the above sequence, 6, 3, 1 is repeating. And the start index of 6 is 2 and repeating length is 3 i.e., 6 repeats after 3 cycle, similarly 3 and 1.
  
print(cycle([1,2,3,4]))
  
Sample Output:
  [] No repeatative cycle.


  
