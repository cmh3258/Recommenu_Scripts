'''

This script is to get fs_ids.
    - go through list of restaurants.
    - call fs
    - save fs_id and fs_restaurant_name

Chris Hume
11/27/13


'''


import foursquare, json
import logging
logging.basicConfig()

client_id = "YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT"
client_secret="2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN"
callback=''

client = foursquare.Foursquare(client_id, client_secret, redirect_uri='http://fondu.com/oauth/authorize')
auth_uri = client.oauth.auth_url()

#Opening file to write to
outfile = open("austin_fsid_temp.txt", "a")

#Declaring some string to save so we can match them up later
fs_name = ''
fs_address = ''
fs_zip = ''
fs_id = ''
count = 0


#input names from boston list
openfile = open("austin_restaurants_randosites.txt", "r")

'''
#dictionary {restaurant_name, url}
boston_names_urls = {}
for line in openfile:
    line = line.strip()
    line = line.split(",")
    boston_names_urls[line[0]] = line[1]
'''

list_count = 0
fs_count = 0

#go through dict and get foursquare id
for name in openfile:
    print 'Name: ', name
    list_count += 1
    result = client.venues.search(params={'query':name, 'near':'Austin,TX', 'llAcc':'100.0', 'limit': '6', 'categoryID' : '4d4b7105d754a06374d81259'})
    for key in result:
       #print 'From FS: '
        #print key, ':', result[key]
        bob = result[key]
        for item in bob:
            #print ' '
            #print item
            #if am_zip in item:
            #	print 'YESIRISE IFJEWL'
            found = False
            for b in item:
		#print b, ':', item[b]
		if b == 'name':
                    #print b, ' : ', item[b], ' : ', am_name 
                    #if item[b] == am_name:
                    #	fs_name = am_name	
                    fs_name = item[b]
                    #print 'fs_name: ', fs_name
		if b == 'id':
                    #print b, ':', item[b]
                    fs_id = item[b].strip()
                    #print fs_id
                    #outfile.write(b + ' : ' + item[b] + '\n---\n')

		    #print am_name , ' : ', fs_name 
                    #print am_zip , ' : ', fs_zip 
                    #print am_address , ' : ', fs_address 
                    #print am_id , ' : ', fs_id 
                    #printnt fs_name, '\n', fs_address, '\n', fs_zip, '\n', fs_id, '\n'
                    fs_name = fs_name.strip()
                    fs_zip = fs_zip.strip()
		    fs_id = fs_id.strip()
		
        
            try:
                #print 'Writing to file--> fs_id:', fs_id, ". fs_Name: ", fs_name, ". Name: ", name
                #print fs_name , " : ", name
                '''
                Might have to do some other sort of matching instead of matching the names lowercased.
                There doesn't seem like there is too many matches.

                With multiple fs_id for a restaurant how will I add menu ratings for the different?
                    - maybe just go thorugh multiple times

                Go thorugh yelp dict and match with rest name, then get ratings.
                '''

                '''
                if(fs_name.lower().strip() == name.lower().strip()):
                    #outfile.write('id: ' + fs_id + '.\tFs_name: ' + fs_name + ".\tName: " + name + '\n')
                    outfile.write(fs_id + "," + fs_name + "," + name + "\n")
                    #print 'Writin'
                    print 'Match: ',fs_name.lower().strip() ,' : ', name.lower().strip()
                    fs_count += 1
                else:
                    print 'No Match:', fs_name.lower().strip() ,' : ', name.lower().strip()
                '''

                #print every fs restaurant that is returned
                outfile.write(fs_id + "," + fs_name + "\n")
                fs_count += 1
                    
            except:
                #outfile.write(fs_id + ' , \n')
                pass
        print "----------------"
        #outfile.write('\n')
outfile.write("Count of Restaurants from file: " + str(list_count))
outfile.write("Count of Restaurants from FourSquare: " + str(fs_count))
outfile.close()
openfile.close()


lines_seen = set() # holds lines already seen
outfile = open("austin_fsid.txt","a")
for line in open("austin_fsid_temp.txt","r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()















