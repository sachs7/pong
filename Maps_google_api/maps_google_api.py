import json
from urllib.request import urlopen
from urllib.parse import urlencode

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
	address = input("Enter Location: ")
	if len(address) < 1:
		break
		
	f = {'sensor': 'false', 'address': address}
	url = serviceurl + urlencode(f)
	print("Retrieving ", url)
	
	data = urlopen(url).read().decode()
	print("Retrieved ", len(data), "characters")
	
	parsed_data = json.loads(data)
	# print(json.dumps(parsed_data, indent=4))
	print(parsed_data["results"][0]['place_id'])
	
Solution:
          $ python Googles_map_api.py
            Enter Location: Michigan
            Retrieving  http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Michigan
            Retrieved  1391 characters
            ChIJEQTKxz2qTE0Rs8liellI3Zc
            
            Enter Location: South Federal University
            Retrieving  http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=South+Federal+University
            Retrieved  2101 characters
            ChIJJ8oO7_B_bIcR2AlhC8nKlok
            
            Enter Location: Universite Catholique de Louvain
            Retrieving  http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Universite+Catholique+de+Louvain
            Retrieved  1912 characters
            ChIJ6abM1HImwkcRwM_ocmCdF7A
