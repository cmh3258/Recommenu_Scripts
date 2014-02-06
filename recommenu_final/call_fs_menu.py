'''

This script is to get fs menus:
    - go through list of fs_ids
    - see if have menu

Chris Hume
12/10/13


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

infile = open("boston_fsid_final_chains.txt", "r")
outfile = open("boston_fsid_final_chains_1.txt","a")

#dictionary= { fs_id , name }
dict_fs = {}
key_count = 0
for line in infile:
    line = line.strip()
    line = line.split(",")
    try:
        dict_fs[line[0]] = line[1]
        key_count += 1
    except:
        pass

#go through and call menu
print 'Keys: ', key_count
for fsid, name in dict_fs.items():
    r = requests.get("https://api.foursquare.com/v2/venues/"+fsid+"/menu?client_secret=2GA3BI5S4Z10ONRUJRWA40OTYDED3LAGCUAXJDBBEUNR4JJN&client_id=YZVWMVDV1AFEHQ5N5DX4KFLCSVPXEC1L0KUQI45NQTF3IPXT")
    key_count -= 1
    print 'Received. Keys left: ', key_count, " ", name
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
                #save_this = True
            except:
                sec_true = False
                print 'excetion'
            try:
                print name, " ;" ,item_id[0], " ; ", item_name
            except:
                pass
        #print save_this
        #print name, " ", fsid

        #will save the restaurant if can get the menu
        try:
            outfile.write(fsid + "," + name + "\n")
        except:
            pass
        first_count += 1
    print 'Done'
outfile.close()

#reduce the outfile if duplicates were added
lines_seen = set() # holds lines already seen
outfile = open("boston_fsid_final_chains_final.txt", "a")
for line in open("boston_fsid_final_chains_1.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()








