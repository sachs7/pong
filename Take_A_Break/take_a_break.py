import webbrowser
import time
import random

already_played = []

playlist = ["https://www.youtube.com/watch?v=D2AnoBH5xYM",
"https://www.youtube.com/watch?v=CJgs2RMtQXo",
"https://www.youtube.com/watch?v=ezcQu1JtcPM",
"https://www.youtube.com/watch?v=0Z33CwdtUIA"]

print("This program started at: ", time.ctime())

break_times = 3

for i in range(break_times):

	""" Wait for 2 hours (7200 seconds) """
	time.sleep(7200) 
	
	song = random.choice(playlist)
	indx = playlist.index(song)
	removed = playlist.pop(indx)
	
	webbrowser.open(song)
	already_played.append(removed)
