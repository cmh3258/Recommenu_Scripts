'''

This script goes through the reduced chains file
and gets the good menus and bad menus

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

#outfile = open("menu_final_2.txt","a")
#nomenu = open("no_menu.txt","a")

word = current_word = ""
has_one_menu = False
#burger key id's
test = ['4a802d77f964a520b6f41fe3','4bfff923369476b0559f8e1f']
for fsid in test:

    r = requests.get("https://api.foursquare.com/v2/venues/"+fsid+"/menu?client_secret=2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN&client_id=YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT")
    #key_count -= 1
    #print 'Received. Keys left: ', key_count, " ", name
    data = r.text
    soup = BeautifulSoup(data)
    js = json.loads(data)
    if data:
        #print 'good'
        print data
        try:
            print js['response']['menu']['menus']['items'][0]['menuId']
            #print 'yes sir'
            #print line + ",y"
            #outfile.write(line + ",y\n")
            has_one_menu = True
        except:
            print 'no menu'
            #outfile.write(line + ",n\n")
    else:
        print 'null'

#outfile.close()
#nomenu.close()








