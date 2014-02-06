'''

Script to get menus from yelp, and save ratings

Name: Chris Hume
Date : 12/6/13


'''


import foursquare, json, requests
import logging
from bs4 import BeautifulSoup
from urllib2 import urlopen
logging.basicConfig()

##############################
#
#	get the individual ratings of each item
#
##############################
def get_ratings(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
 
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



#r = requests.get("http://www.yelp.com/menu/mistral-restaurant-boston/item/grilled-portobello-mushroom-carpaccio")
#r = requests.get("http://www.yelp.com/menu/mistral-restaurant-boston/item/seared-foie-gras")

##############################
#
# 	Need to call get_menu.py -- (add as a funciton)
#	then request that url if get (url) and skip (if == False)
#
##############################

#r = requests.get("http://www.yelp.com/menu/mistral-restaurant-boston/")
r = requests.get("http://www.yelp.com/menu/coda-boston")
count = 0

data = r.text
soup = BeautifulSoup(data)

'''
for link in soup.find_all('a'):
	#print (link.get('href'))
	#if(link.get('href').find('grilled')):
	#	print link.get('href')
	bob = str(link.get('href'))
	sub = 'grilled'
	if(sub in bob):
		addon = link.get('href')
		#print addon
		full_url = "http://www.yelp.com"+addon
		print full_url
		r = requests.get(full_url)


the class we need is = "menu-item-details"
	then need the link in this class 
	need to save the menu item
'''
def is_item(tag):
	return tag.has_attr()

#print soup.find_all("div", "menu-item-details")
###################################
#
#	Need to find links inside class = "menu-item-details"
#
#	Dictionary of html links and item names
#
###################################
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
yelp_menu = {}
yelp_count = 0
for key, value in name_and_url.items():
	print key
	print value, '\n'
	yelp_menu[key] = value
	yelp_count += 1
        #print get_ratings(value)

fsid = "49fb1332f964a520166e1fe3"
r = requests.get("https://api.foursquare.com/v2/venues/"+fsid+"/menu?client_secret=2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN&client_id=YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT")
data = r.text
soup = BeautifulSoup(data)
js = json.loads(data)
#print data

#print js['response']['menu']['menus']['items'][0]['menuId']
first_true = True
save_this = False
first_count = 0
item_name = ""
item_id = 0
fs_menu = {}
fs_count = 0
while(first_true):
        sec_count = 0
        sec_true = True
        try:
                js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['name']  
        except:
                first_true = False
                break
        while(sec_true):
                #save the id and anme
                try:
                        item_id = js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['entries']['items'][sec_count]['entryId']
                        item_name = js['response']['menu']['menus']['items'][0]['entries']['items'][first_count]['entries']['items'][sec_count]['name']
                        sec_count += 1
                        fs_menu[item_name] = item_id
                        fs_count += 1
                        #save_this = True
                        #print item_id
                except:
                        sec_true = False
                        #print 'exception'
                try:
                        #print item_id, " ; ", item_name
                        pass
                except:
                        pass
                #print save_this
                #print name, " ", fsid

                #will save the restaurant if can get the menu
        try:
                pass
                #outfile.write(fsid + "," + name + "\n")
        except:
                pass
        first_count += 1
print 'Done'
print 'fs_items : ', fs_count
print 'yelp_items : ', yelp_count

match_count = miss_count = 0
for name, value in fs_menu.items():
        #print name
        name = name.strip()
        name = name.lower()
        try:
                en = yelp_menu[name]
                #print 'Yes: ', en
                match_count += 1
        except:
                #print 'No: ', name
                miss_count += 1


print 'match_count: ', match_count
print 'miss_count: ', miss_count




###################################
#
#	Go through each word and add to dictionary 
#	match with recomenuAPI data - id
#
###################################

'''
openfile = open("results_db.txt", "r")

name_and_ids = {}
for line in openfile:
	line = line.strip()
	line = line.split('|')
	#print line[2], " : ", line[3]
	name = line[2]
	id = line[3]
	name = name.lower()
	name_and_ids[name] = id

#for key, value in name_and_ids.items():
#	print key, value

openfile.close()


###################################
#
#	Go through dictionary - go to urls, get ratings
#	save into a dictionary
#
###################################

	

testingdict = {}
testingdict["help"] = [1, 2, 3]
for key, value in testingdict.items():
	print key, value

id_and_ratings = {}
for name, url in name_and_url.items():
	#print name, " : ", url
	print get_ratings(url)
	id = name_and_ids.get(name)
	print id, " : ", name
	
	#########
	#
	#	Maybe just need to save {item_name, ratings}
	#
	#########
	

'''


