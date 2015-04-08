g_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(string, shiftkey):
	
	""" Shift 'g_list' by 'shiftkey' places """
	b_list = g_list[shiftkey:] + g_list[:shiftkey]
	
	""" To hold final result """
	res = ""
	res_space = " "    
	
	""" Split the given string by space """
	word_list = string.split(" ")
	
	""" If given string is 'space' then return as it is """
	if string == " ":
		return res_space
		
	""" Loop through the list of items from 'word_list' """	
	for i in word_list:
		for j in i:
			if j.isalpha() and j.isupper():
				
				""" If letter is in uppper case then convert it into lowercase """
				j = j.lower()
				
				""" Find the index of the element in g_list and map it on to the corresponding element in b_list """
				g_indx = g_list.index(j)
				c_indx = b_list[g_indx]
				res += c_indx.capitalize()
				
			elif j.isalpha():
				
				""" If letter is not uppercase """
				g_indx = g_list.index(j)
				c_indx = b_list[g_indx]
				res += c_indx
			else:
				
				""" for all the elements like space, commas, exclamation """
				res += j
				
		res += " "
	res = res.rstrip(" ")
	return res
	
msg = input("Enter message: ")
shift_amt = int(input("By what amount you want to shift? Keep between [-25 to 25]: "))

print(caesar(msg, shift_amt))


Sample Output:
	
	Enter message: Awesome! I can send cipher messages now!...;)
	By what amount you want to shift? Keep between [-25 to 25]: -8
	Sowkgew! A usf kwfv uahzwj ewkksywk fgo!...;)
