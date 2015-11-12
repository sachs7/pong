from urllib.request import urlopen
import xml.etree.ElementTree as etree


# address = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml"

address = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171034.xml"

ur = urlopen(address).read()
print('Retreived ', len(ur), ' characters')

data = etree.fromstring(ur)
sum = 0

for i in range(len(data.findall('.//count'))):
	s = data.findall('.//count')[i].text
	sum += int(s)
print(str(sum))

Solution: $ python xml_parser.py
          Retreived  4205  characters
          2821
