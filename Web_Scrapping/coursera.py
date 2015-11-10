from urllib.request import urlopen
from bs4 import *

def parsing(url, count, pos):
	if 0 < count < count+1 :
		html = urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")
		tags = soup('a')	
		
		url = tags[pos].get('href')
		count -= 1
		if count == 0:
			print("Last URL: ", url)
		else:
			print("Retrieving: ", url)
		parsing(url, count, pos)

		
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
parsing("http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Riha.html", count, pos-1)

Soultion:
        Enter count: 7
        Enter position: 18
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Hugh.html
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Beinn.html
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Janna.html
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Vuyolwethu.html
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Keigan.html
        Retrieving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Safi.html
        Last URL:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Atlanta.html
