def count_say(number):

	result = 1
	temporary = []

	if len(number) == 1:
		temporary.extend([str(result)+str(number)])
		return str(result)+str(number)

	for i in range(1, len(number)):
		if number[i-1] == number[i]:
			result += 1
		else:
			temporary.extend([str(result)+str(number[i-1])])
			result = 1

	temporary.extend([str(result)+str(number[i])])
	result = 1
	return ''.join(temporary)

print(count_say('11342122112'))
Output: 2113141211222112

print(count_say('1'))
Output: 11

print(count_say('890132'))
Output: 181910111312
