
def rgb(r, g, b):
	res = ""
	if 0 <= r <= 255:
		firs = bin(r)
	
		firs_hex = hex(int(firs, 2))
		firs_hex = firs_hex[2:]
		if len(str(firs_hex)) < 2:
			res += "0" + str(firs_hex)
		else:
			res += firs_hex
	elif r > 255:
		res += "FF"
	else:
		res += "00"
		
	if 0 <= g <= 255:	
		sec = bin(g)

		sec_hex = hex(int(sec, 2))
		sec_hex = sec_hex[2:]
		if len(str(sec_hex)) < 2:
			res += "0" + str(sec_hex)
		else:
			res += str(sec_hex)
	elif g > 255:
		res += "FF"
	else:
		res += "00"
	
	if 0 <= b <= 255:
		thir = bin(b)
	
		thir_hex = hex(int(thir, 2))
		thir_hex = thir_hex[2:]
		if len(str(thir_hex)) < 2:
			res += "0" + str(thir_hex)
		else:
			res += str(thir_hex)
	elif b > 255:
		res += "FF"
	else:
		res += "00"
		
	return res.upper()

print(rgb(88, 188, 255))

Sample Output:
          58BCFF
