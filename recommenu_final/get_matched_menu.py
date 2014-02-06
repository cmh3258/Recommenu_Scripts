'''


Script that takes {fs_rest_name, fs_id} and {fs_rest_name, yelp_menu_url}
    - then matches them up


Chris Hume
12/9/13


'''
import foursquare, json, requests, sys
import logging
from bs4 import BeautifulSoup
from urllib2 import urlopen
logging.basicConfig()



#gets link for each menu item
def get_menu_item_url(url, name, fsdict):
    r = requests.get(url)
    print url, " ", name, " ", fsdict[name+""]
    count = 0

    data = r.text
    soup = BeautifulSoup(data)
    name_and_url = {}
    list_of_items = []
    line = soup.find_all("div", class_="menu-item-details")
    count = 0
    for x in line:
            #print x
            #print 'yes\n'
            x = x.find("a")
            try:
                    #print x.get('href')			#link to the menu item
                    count += 1
                    #list_of_items.append(x.getText())	#name of the menu item
                    url = x.get('href')	
                    full_url = "http://www.yelp.com"+url
                    name = x.getText()
                    name = name.lower()
                    name_and_url[name] = full_url		# add to dict={name, url}
                    full_url = ''
            except:
                    print '',
    #print count
    for key, value in name_and_url.items():
            #print key
            #print value, '\n'
            print get_ratings(value)    #calls get_ratings on each menu item url
    

##############################
#
#	get the individual ratings of each item
#
##############################
def get_ratings(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)

        #print 'Getting ratings'
	##################################
	#
	#	Getting the ratings for the item
	#
	##################################
	five_star = four_star = three_star = two_star = one_star = null_star = 0
	word = soup.find_all("i", class_="star-img stars_5")
	for x in word:
		#print word
		five_star += 1


	word = soup.find_all("i", class_="star-img stars_4")
	for x in word:
		#print word	
		four_star += 1
	
	word = soup.find_all("i", class_="star-img stars_3")
	for x in word:
		#print word
		three_star += 1


	word = soup.find_all("i", class_="star-img stars_2")
	for x in word:
		#print word
		two_star += 1


	word = soup.find_all("i", class_="star-img stars_1")
	for x in word:
		#print word
		one_star += 1


	word = soup.find_all("i", class_="star-img stars_0")
	for x in word:
		#print word
		null_star += 1

	likes = five_star + four_star + three_star
	dislikes = null_star + one_star + two_star
	#neutral = three_star + two_star

	#print likes, " : ", neutral, " : ", dislikes	
	return [likes, dislikes]

def match_step(fsid, yelpurl):
    #print 'in match step'
    fs_id = fsid.strip()
    r = requests.get("https://api.foursquare.com/v2/venues/"+fs_id+"/menu?client_secret=2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN&client_id=YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT")
    #print r
    data = r.text
    soup = BeautifulSoup(data)
    js = json.loads(data)
    #print data

    #print js['response']['menu']['menus']['items'][0]['menuId']
    fs_menu = {}
    first_true = True
    first_count = fs_count = 0
    #print 'in loop'
    while(first_true):
        sec_count = 0
        sec_true = True
        try:
            js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['name']
        except:
            first_true = False
            break
        
        while(sec_true):
            try:
                item_id = js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['entries']['items'][sec_count]['entryId']
                item_name = js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['entries']['items'][sec_count]['name']
                fs_menu[item_name.lower()] = item_id
                fs_count += 1
                sec_count += 1
            except:
                sec_true = False
        first_count += 1
    #print 'Done'

    #now call to match with yelp menu items
    yelp_match(fs_menu, yelpurl)

#this menu is from restA and url is from restA
#so its from one restaurant, not a list
def yelp_match(fs_menu, yelpurl):
    r = requests.get(yelpurl)
    count = 0

    data = r.text
    soup = BeautifulSoup(data)

    name_and_url = {}
    list_of_items = []
    line = soup.find_all("div", class_="menu-item-details")
    count = 0
    
    #this gets each item url
    for x in line:
            #print x
            #print 'yes\n'
            x = x.find("a")
            try:
                    #print x.get('href')			#link to the menu item
                    count += 1
                    #list_of_items.append(x.getText())	#name of the menu item
                    url = x.get('href')	
                    full_url = "http://www.yelp.com"+url
                    name = x.getText()
                    name = name.lower()
                    name_and_url[name] = full_url		# add to dict={name, url}
                    full_url = ''
            except:
                    pass
    #print count
    yelp_menu = {}
    yelp_count = 0
    for key, value in name_and_url.items():
            #print key
            #print value, '\n'
            yelp_menu[key] = value
            yelp_count += 1
    
    #for item, fsid in fs_menu.items():
    #this is matching up yelp with fs
    writefile = open("item_ratings_austin_new.txt", "a")
    for name, url in yelp_menu.items():
        #if try works, then can get the ratings for it.
        try:
            fsid = fs_menu[name]
            #print 'yes'
            #now go get ratings
            rating_list = get_ratings(url)
            yelp_count -= 1
            print 'Writing...', yelp_count
            writefile.write(fsid)
            for item in rating_list:
                #print item
                writefile.write("," + str(item))
            writefile.write("\n")
            #print '...writen'
            #then save it into a new dictionary
                #dict = {fs_item_id, ratings}
                #then write that to a file
             
        except:
            #print 'no'
            pass

    print 'Got the Ratings'
    writefile.close()
    
def main():


    client_id = "YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT"
    client_secret="2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN"
    callback=''
    
    client = foursquare.Foursquare(client_id, client_secret, redirect_uri='http://fondu.com/oauth/authorize')
    auth_uri = client.oauth.auth_url()
    
    fsid_name = {}  #dictionary with fs ids and fs
    fs_count = 0
    infile= open("austin_fsid_final.txt", "r")
    for line in infile:
        #print line
        line = line.strip()
        #print line
        line = line.split(",")
    
        #save the fs_ids and names into dictionary
        fs_id = line[0].strip()
        name = line[1].strip()
        fsid_name[name] = fs_id
        fs_count += 1
    infile.close()

    
    '''
    Now need to get the yelp_menu_item_names, yelp_menu_item_url     
    '''
    infile = open("fsname_yelpurl_austin.txt", "r")
    yelp = {}
    for line in infile:
        line = line.strip()
        line = line.split(",")
        restname = line[0]
        menurl = line[1]
        yelp[restname] = menurl
        #print restname, " ", menurl
        #print get_menu_item_url(menurl, restname, fsid_name)
        #print 'Next item...'
    
    
    '''
    
    - Matching the fs_rest_name with url.
    - if there is a match need to get fs item, then ratings from yelp
    
    - good way:
        - pass in fsid, yelpurl into a function
        - will call fsid, save the {item_name, item_id}
        - then call yelpurl, matching with fs_item_name:
            - if match: then save/get ratings
    
    '''


    #need to keep track of which restaurants we went through already
    outfile = open("track_of_rest_match_austin.txt","a")
    outfile.close()
    outfile = open("track_of_rest_match_austin.txt","r")
    rest_exist = {}
    for x in outfile:
        x = x.strip()
        rest_exist[x] = ""
    outfile.close()
    outfile = open("track_of_rest_match_austin.txt","a")
    good = 0
    bad = 0
    for restname, fsid in fsid_name.items():
        if fsid in rest_exist:
            print 'Match.'
            continue
        fs_count -= 1
        print 'FS Left: ', fs_count
        outfile.write(fsid+"\n") #this needs to be fsid's instead of names
        try:            
            url = yelp[restname]
            print yelp[restname]
            good += 1
            match_step(fsid, url)
            #break
        except:
            bad += 1
            pass
    print good
    print bad   #will need to find a better way to add restaurants with similar names
    
    outfile.close()
main()

