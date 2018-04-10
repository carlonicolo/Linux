import os

os.system('ls /usr/share/nano/ >> ~/.nanorc')

with open(os.path.expanduser('~/.nanorc'), 'r') as file:
    # read a list of lines into data
    data = file.readlines()

print(data)
#print "Your name: " + data[0]

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
