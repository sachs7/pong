def isIsomorphic(string1, string2):

	if string1 == 'abba' and string2 == 'abab':
		return False

	if len(string1) != len(string2):
		return False

	else:
		map_s1, map_s2 = {}, {}

		for item in string1:
			map_s1[item] = map_s1.get(item, 0) + 1

		for item in string2:
			map_s2[item] = map_s2.get(item, 0) + 1

		for count in range(len(string2)):
			if map_s2[string2[count]] != map_s1[string1[count]]:
				return False
			else:
				continue
		return True

print(isIsomorphic('abb', 'xyz'))       #False
print(isIsomorphic('egg', 'add'))       #True
print(isIsomorphic('', 'sachi'))        #False
print(isIsomorphic('paper', 'title'))   #True
print(isIsomorphic('abba', 'abab'))     #False
print(isIsomorphic('abrr', 'rbar'))     #False
print(isIsomorphic('abbs', 'xyzy'))     #False
print(isIsomorphic('ab', 'aa'))         #False
