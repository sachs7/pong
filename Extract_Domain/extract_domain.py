import re

def domain_name(url):
	pat_url = re.compile(r"([\w]+[\-\w]+[\w])")
	res = re.findall(pat_url,url)

	if res[0] == "http" and res[1] != "www":
		return res[1]
	elif res[0] == "http" and res[1] == "www":
		return res[2]
	elif res[0] == "www":
		return res[1]
	else:
		return res[0]
	

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("google.com"))
print(domain_name("www.cnet.com"))

Sample Output:
              github
              zombie-bites
              google
              cnet
