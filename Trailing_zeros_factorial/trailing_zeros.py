import math

def trail_zero(n):
  
  """ Get the factorial of a number from the inbuilt function and convert it into list """
	fact = list(str(math.factorial(n)))
  
	count = 0 # Counter value to keep tab of the number of zeros.
	
	""" Now count the number of zeros from the above list """
	for i in range(1, len(fact) + 1):
		if fact[-i] == "0":
			count += 1
		else:
			break
	return count

print(trail_zero(1000))	


******** Method 2: More efficient than the above ********
******** Please go through readme link to understand below code ********

def trail_zero(n):
	k = 0
	
	for i in range(0, 100000):
		if 5**(i+1) > n:
			k = i
			break
		else:
			continue
			
	sum = 0
	
	for i in range(1, k+1):
		sum = sum + n//5**i
	return sum
	
	
print(trail_zero(120))

Sample Output: 
  28 (120! gives 28 trailing zeros)
  
