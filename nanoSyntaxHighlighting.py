import os
from pathlib import Path
import sys


def readWriteNanorc():
	""" This function open the file .nanorc reading line by line
	store the file in the variable data.
	At this point modifies line by line adding 'include' and the '\n' newline.
	Finally writes the content. 
	"""
	try:
		with open(os.path.expanduser('~/.nanorc'), 'r') as file:
	    # read a list of lines into data
		    data = file.readlines()
		
		print(data)
		
		i=0
		for d in data:
		    print("Type d: ",type(d), " Type data: ", type(data))
		    print("Old d: ", d)
		    
		    #print("Position -2: ",d[-3])
		    d = 'include "'+d[:-1]+'"'+d[-1:0]
		    data[i] = d+"\n"
		    
		    #s[:4] + '-' + s[4:]
		    
		    print("New d: ", d)
		    i=i+1
		    
		print(data)

		# and write everything back
		with open(os.path.expanduser('~/.nanorc'), 'w') as file:
		    file.writelines( data )
	except:
		print("Something Unexpected has happened.",sys.exc_info()[0])


try:
	#variable using to check if .nanorc exists
	nanorc_file = Path(os.path.expanduser('~/.nanorc'))

	#checking if .nanorc exists
	if nanorc_file.exists():
		print("nanorc exists")

		#rename the .nanorc file if exists
		os.rename(os.path.expanduser('~/.nanorc'), os.path.expanduser('~/.nanorc_old'))
		
		#create .nanorc redicting the ls command result
		os.system('ls /usr/share/nano/ >> ~/.nanorc')

		#call function
		readWriteNanorc()
	else:
		print("nanorc file doesn't exists")
		
		#create .nanorc redicting the ls command result
		os.system('ls /usr/share/nano/ >> ~/.nanorc')
		
		#call function
		readWriteNanorc()
except:
    print("Something Unexpected has happened.",sys.exc_info()[0])