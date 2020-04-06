# Python Code
# Opening a google map in a browser and taking from clipboard or command 
import sys,webbrowser,pyperclip

# here sys is for command line argv is what we will type if its greater than 1
# We added / joined that data and gave it to add.
if len(sys.argv)>1:
	add = ''.join(sys.argv[1:])	
else:
	add = pyperclip.paste()
#pyperclip is used for clipboard	
webbrowser.open('www.google.com/maps/search/?api=1&query='+add)
# now above link is for opening and searching maps
# Searching example : 
# New York
# Aurangabad
# Rajasthan