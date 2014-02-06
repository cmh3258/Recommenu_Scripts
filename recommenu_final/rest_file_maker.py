'''

Need to make a file with restaurants - this is just a temp script

Chris Hume
12/7/13

'''

infile = open("fsname_yelpurl.txt", "r")
currfile = open("current_rest.txt","a")

for line in infile:
    line = line.strip();
    line = line.split(",");
    name = line[0]
    currfile.write(name+"\n")
    
