write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py

Test your program with the real Google API:

http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=University+of+Michigan

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

$ python solution.py
Enter location: South Federal University 
Retrieving http://...
Retrieved 2101 characters
Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok 

Source: Coursera
