from urllib.request import urlopen
import json


# address = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json"

address = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171038.json"

ur = urlopen(address).read().decode()
print("Retreiving: ", address)
print('Retreived ', len(ur), ' characters')

data = json.loads(ur)
print("Count: ", len(data['comments']))
# print(json.dumps(data, indent=4))
sum = 0
for i in range(len(data["comments"])):
	sum += int(data['comments'][i]['count'])
print("Sum: ", str(sum))

Solution:
        $ python json_parser.py
          Retreiving:  http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171038.json
          Retreived  2730  characters
          Count:  50
          Sum:  2252
