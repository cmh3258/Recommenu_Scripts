'''
Just checking to see how many matches we get from
foursquare ids + yelp restaurants

1/20/14
Chris Hume
Recommenu

'''
#au = open("austin_fsid_final.txt","r")
fifi = open("fsname_yelpurl_austin.txt","r")
total = match = 0
for line in fifi:
    line = line.split(",")
    rn = line[0].strip().lower()
    total += 1
    au = open("austin_fsid_final.txt","r")
    for x in au:
        x = x.split(",")
        name = x[1].strip().lower()

        if name == rn:
            match += 1
            break
        
    au.close()
print "Total: " , total
print "Match: " , match


fifi.close()
