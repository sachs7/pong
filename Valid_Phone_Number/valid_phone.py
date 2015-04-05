import re

def valid_phone(num):
	pattern = re.compile(r'^\(\d{3}\)[ ]\d{3}-\d{4}$')
	if pattern.search(num):
		return True
	else:
		return False
