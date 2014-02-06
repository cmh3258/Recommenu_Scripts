'''

This script is to get fs_ids of menus from chain restaurants
    - there are chains of restaurants - say Chickfila
    - some chickfilas say they have a menu, and some do not
        - need to map not working ones, to a working one

Chris Hume
1/17/14


'''


import foursquare, json, requests
import logging
from bs4 import BeautifulSoup
from urllib2 import urlopen
logging.basicConfig()

client_id = "YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT"
client_secret="2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN"
callback=''

client = foursquare.Foursquare(client_id, client_secret, redirect_uri='http://fondu.com/oauth/authorize')
auth_uri = client.oauth.auth_url()

#Opening file to write to
outfile = open("menu_temp.txt", "a")

#Declaring some string to save so we can match them up later
fs_name = ''
fs_address = ''
fs_zip = ''
fs_id = ''
count = 0


#input names from boston list
openfile = open("chains.txt", "r")

#openfile = ['Chickfila']

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
fs_list = []

#go through dict and get foursquare id
for name in openfile:
    print 'Name: ', name
    list_count += 1
    result = client.venues.search(params={'query':name, 'near':'Boston,MA', 'llAcc':'100.0', 'limit': '50', 'categoryID' : '4d4b7105d754a06374d81259'})
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
                    try:
                        print 'fs_name: ', fs_name
                    except:
                        pass
		if b == 'id':
                    print b, ':', item[b]
                    fs_id = item[b].strip()
                    fs_list.append(fs_id)
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
		if b == 'location':
		    #print 'this is the right one'
		    #print b, ':', item[b]
                    sandy = item[b]
                    #printnt sandy
		
                    # Get the ZIP and ADDRESS
                    for x in sandy:
			#print x, ':', sandy[x]
                        if x == 'postalCode':
                            #print sandy[x]
                            san = sandy[x]
                            san = san.strip()
                            fs_zip = san
                            #print fs_zip
			if x == 'address':
                            #print sandy[x]
                            san = sandy[x]
                            san = san.strip()
                            fs_address = san
                            print fs_address
                            #print fs_address
                        if x == 'city':
                            print sandy[x]
                    print ''
        
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
                #print 'Writing'
                #outfile.write(fs_id + "," + fs_name + "\n")
                pass
        print "----------------"
        #outfile.write('\n')

 
#outfile.write("Count of Restaurants from file: " + str(list_count) + "\n")
#outfile.write("Count of Restaurants from FourSquare: " + str(fs_count))
#openfile.close()
outfile.close()

lines_seen = set() # holds lines already seen
outfile = open("menu_temp_final.txt","a")
for line in open("menu_temp.txt","r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

'''
outfile = open("menu_final.txt","a")
for line in open("menu_temp_final.txt","r"):
    line = line.strip()
    ray = line.split(",")
    fsid = ray[0]
    
    r = requests.get("https://api.foursquare.com/v2/venues/"+fsid+"/menu?client_secret=2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN&client_id=YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT")
    #key_count -= 1
    #print 'Received. Keys left: ', key_count, " ", name
    data = r.text
    soup = BeautifulSoup(data)
    js = json.loads(data)
    if data:
        print 'good'
        #print data
        try:
            js['response']['menu']['menus']['items'][0]['menuId']
            print 'yes sir'
            #print line + ",y"
            outfile.write(line + ",y")
        except:
            print 'no menu'
            outfile.write(line + ",n\n")
    else:
        print 'null'

outfile.close()



Will need to go through the list of returned restaurnts and save
the ones that have menus and the ones that do not.

how should from list?

Mcdonalds
Good
234554
432593819
32819
Bad
324344
35435
874335


'''













