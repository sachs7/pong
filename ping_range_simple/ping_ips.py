import re
import subprocess as sp

""" Search for below pattern in the 'ping' response. Make sure to 
	search for 'bytes (b)' {re.compile(b'')} and not string (r) {re.compile(r'')}
"""
pattern1 = re.compile(b"unreachable")
pattern2 = re.compile(b"timed out")

ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

def ip_status(ip, rnge):
	
	""" List to hold active IP addresses """
	active = []
	down = []
	timed_out = []
	
	""" Get the first 3 fields of IP """
	addres = ip.split(".")[:3]
	ne_ip = ".".join(addres)
	
	""" Get the last field of IP """
	lst_field = ip.split(".")[3]
	
	if rnge == "0" or rnge == "":
		rnge = 1
	
	if 0 <= int(rnge) <= 255 and ip_pattern.match(ip):
		""" Calculate the actual range """
		actual_rnge = int(lst_field) + int(rnge)

		""" Range of IP address to be pinged """
		""" Right now it starts from 0 through 10 but can be changed in the below line """
	
		for i in range(int(lst_field), actual_rnge):		
		
			ip_fin = ne_ip + "." + str(i)
			status  = sp.check_output(["ping ", ip_fin])
		
			if pattern1.search(status) :
				down.append(ip_fin)
			elif pattern2.search(status):
				timed_out.append(ip_fin)
			else:
				active.append(ip_fin)
	
		result = "\nActive IP addresses are: " + str(active) + "\n\n" + "Unreachable IP: " + str(down) + "\n\n" + "Timed out IP's: " + str(timed_out)
		return result
	
	else:
		return "1) Range should be in between 0 and 255 inclusive. \n2) Check the IP format."
		
		
ip = input("Enter the IP address eg., 10.0.0.1:   ")
rnge = input("Enter the range of IP's: ")

print(ip_status(ip, rnge))

Sample Output:
	Enter the IP address eg., 10.0.0.1:   10.0.0.7
	Enter the range of IP's: 5

	Active IP addresses are: ['10.0.0.10']

	Unreachable IP: ['10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.11']

	Timed out IP's: []
	
	
	Enter the IP address eg., 10.0.0.1:   10.0.d.c
	Enter the range of IP's: 895
	1) Range should be in between 0 and 255 inclusive. 
	2) Check the IP format.
