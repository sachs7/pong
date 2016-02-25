import webbrowser
import time
import random

already_played = []

playlist = ["https://www.youtube.com/watch?v=D2AnoBH5xYM",
"https://www.youtube.com/watch?v=CJgs2RMtQXo",
"https://www.youtube.com/watch?v=ezcQu1JtcPM",
"https://www.youtube.com/watch?v=0Z33CwdtUIA"]

print("This program started at: ", time.ctime())

for i in range(3):

	""" Wait for 2 hours (7200 seconds) """
	time.sleep(7200) 
	
	song = random.choice(playlist)
	indx = playlist.index(song)
	removed = playlist.pop(indx)
	if song not in already_played:
		webbrowser.open(song)
		already_played.append(removed)
