'''


Script to get the menus some site
    - for boston restaurant


Chris Hume
12/6/13


'''
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests, sys

def call_url(name, url):
    print 'call: ', url
    r = requests.get(url)
    #print r
    #print r.text
    data = r.text
    soup = BeautifulSoup(data)
    #return get_list(soup)
    #return get_yelp_list(soup)
    #return get_bostoncom_list(soup)
    #print 'calling...'
    return get_rest_url(name, soup)   #return dictionary

def get_rest_url(rname, soup):
    rest_list = []
    line = soup.find_all("a", class_="biz-name")
    #print 'get...', line
    result_count = 0
    for x in line:
        if result_count == 4:
            break
        print 'in for...', result_count
        name = x.getText()
        url = x.get('href') #get the url to forum results
        #print url
        full_url = "http://www.yelp.com"+url
        #print full_url
        rest_list.append(full_url.strip())
        #full_list = get_menu_urls(rest_list)
        result_count += 1
    full_list = call_rest_url(rname, rest_list)
    return full_list


#call list of urls
def call_rest_url(name, list_urls):
        #want to call each url and get the menus if the exist
        #do i want to save to file? - lets try
        new_list = {}
        temp_list = []
        for x in list_urls:
                #print 'In call_rest_url loop...'
                x = x.strip()
                #print 'Url:', x
                r = requests.get(x)
                #r = requests.get("http://www.yelp.com/biz/el-pel%C3%B3n-taquer%C3%ADa-boston-3#query:tacos")
                count = 0

                data = r.text
                soup = BeautifulSoup(data)
        
                #########
                #
                #           I am getting the title of the restaurant that we are scraping
                #
                #########
                try:
                        title = soup.find("meta", {"property":"og:title"})['content']
                        print 'Title 1: ', title
                        print 'Title 2: ', name
                        temp_list = get_menu(soup, title)
                        print 'Results: ' ,temp_list[0], " : ", temp_list[1]
                        #new_list.update(temp_list[0], temp_list[1]) #title, url
                        new_list[title] = temp_list[1]
                        print '--New_List has been Updated\n'
                except:
                        #print 'Didnt work!\n'
                        continue
        return new_list


#getting the menu links
def get_menu(soup, title):
        print 'in here'
        try:
        	line = soup.find_all("div", class_="yelp-menu")
        	for x in line:
                        print 'looping'
                        x = x.find("a")
                        url = x.get('href')	
                        full_url = "http://www.yelp.com"+url
                        name = x.getText()
                        #print full_url, " ", name
                        exp = "Full menu"
                        name = name.strip(" ")
                        #print exp, " : ", name
                        if name == exp:
        			print 'This is a Yelp Menu - returning'
                                ##########
                                #
                                #  Will return url 
                                #
                                ##########
                                arr = []
                                arr.append(title)
                                arr.append(full_url)
                                #for x in arr:
                                #       print x
                                return arr
                        else:
        			print 'This is NOT a Yelp menu'
                                ##########
                                #
                                #  Will return False
                                #
                                ##########
                                return [title, ""]
        		
        
        except:
                #print 'This is NOT a Yelp menu(x2)'
                return [title, ""]



def main():
        #url = "http://boston.eater.com/archives/2013/07/09/the-38-essential-boston-restaurants-june-2013.php"
        #list of boston urls from yelp:
        #url = "http://www.yelp.com/search?cflt=restaurants&find_loc=Boston%2C+MA%2C+USA"

        #url = "http://www.yelp.com/search?find_desc=forum&find_loc=boston%2C+ma&ns=1"
        url = "http://www.yelp.com/search?find_desc=mistral&find_loc=boston%2C+ma&ns=1"

        list_restaurants = {}
        full_list = {}
        '''

        need to go through list of restaurant names and
        call urls accordingly
        
        '''
        fsid_name = {}  #dictionary with fs ids and fs names
        total_count = 0
        infile= open("boston_fsid_final_chains.txt", "r")
        for line in infile:
            print line
            line = line.strip()
            #print line
            line = line.split(",")

            #save the fs_ids and names into dictionary
            fs_id = line[0].strip()
            name = line[1].strip()
            fsid_name[name] = fs_id
            
            line = line[1]
            line = line.split(" ")
            sub_str = ""
            for x in line:
                sub_str += x+"+"
            sub_str = sub_str[0:-1]
            #print sub_str[0:-1]
            url = "http://www.yelp.com/search?find_desc="+sub_str+"&find_loc=boston%2C+ma&ns=1"
            url = "http://www.yelp.com/search?find_desc="+sub_str+"&find_loc=austin%2C+tx&ns=1"

            # i want to save the restaurant name
            ###
            # need to save the fsid too...
            ###
            list_restaurants[name] = url
            total_count += 1
            
        #sys.exit()
        infile.close()

        #final file of FS_Restaurants and Yelp_urls
        '''
        infile = open("fsname_yelpurl.txt","r")
        current_rest_count = 0
        fs_yelp_final = {}
        for line in infile:
            line = line.strip()
            line = line.split(",")
            word = line[0]
            url = line[1]
            fs_yelp_final[word] = url
            current_rest_count += 1
        infile.close()
        '''
        currfile = open("current_rest_boston2.txt","a")
        currfile.close()
        
        currfile = open("current_rest_boston2.txt","r")
        current_rest_count = 0
        fs_yelp_final = {}
        for line in currfile:
            line = line.strip()
            fs_yelp_final[line] = ""
            current_rest_count += 1
        currfile.close()

        currfile = open("current_rest_boston2.txt","a")
        yelp_name_url = {}  #dictionary with yelp names and menu urls
        infile = open("fsname_yelpurl_boston_2.txt","a")
        for name, url in list_restaurants.items():
            print '\nTotal # of restaurants left: ', total_count
            print 'Current Rest Count: ', current_rest_count
            print 'Rest Name: ', name #, '->',url
            
            if name in fs_yelp_final:
                print 'Match.'
                total_count -= 1
                continue
            
            #write name to file
            print 'Writing Rest Name - current_rest.txt'
            currfile.write(name+"\n")
            current_rest_count += 1
            #print 'Next..'
            total_count -= 1
            temp_list = call_url(name, url)


            #######################################

            #######################################
            '''
  ----->          We need to have a check to see if the restaurant we got is the same, but
  ----->          with different restaurant names - slightly
            '''
            #######################################

            #######################################
            for rname, rurl in temp_list.items():
                print rname
                full_list[rname] = rurl
                try:
                    #print x, " ", y
                    if rurl=="":
                        print 'passing'
                        pass
                    else:
                        print 'Writing ', rname , ', ', rurl, ' to ', 'file.'
                        yelp_name_url[rname] = rurl     #fs_rest_name, with yelp_menu_url
                        infile.write(rname + "," + rurl + "\n")
                    #print 'Done.'
                except:
                    pass

        infile.close()
        currfile.close()

        '''
        for x, y in fsid_name.items():
            print x,",", y


        '''
        '''
            Will need to save {rest_name, rest_item_name, item_rating}

            Then go through foursquare and save {fs_item_name, fs_item_id}

            Match up names. Then save {ratings, fs_id}

                -- Should I go through and match with foursquare first? So
                    don't have as many calls to yelp? Probably a good idea.

                -- Will need to keep track once again on which yelp rest I call
                    cause yelp will shut me off if call too many times

            call function passing through dictionary with fs and yelp
        '''

            
        



        #
        #will now need to go through yelp_name_url={name, url} and fsid_name={name, id} dictionaries
        #
        #if yelp_name_url{} has foursquare id, then will save fs menu into dict,
        #   then will save yelp menu into a dictionary
        #
        #Once have those two dictionaries, will need to see if the menus have matching items.
        #   save the mathcing into a dictionary = {}
        '''
        for each restaurant:
        
            yelp menu = item_name, url
            fs menu = item_name, fs_item_id

            need to have a new fs_menu_dict that only has yelp items with ratings
            so:
            for yelp_name, url in yelp_menu.items():
                if fs_menu[yelp_name]:
                    url = yelp_menu[name]
                    call url to get the ratings
                    save into dict = bob{item_name, rating}
                    then get fs_id:
                        fs_item_id = fs_menu[item_name]
                        yelp_rating = bob[item_name]
                    new dict = {fs_item_id, yelp_rating}

            will need to save the new_idct into a larger dictionary/global dict.
                - will just add onto this with each new restaurant.
                - will have fs_item_id with yelp_rating.
                **we will actually just save it to a file so we can save it there.

    
        '''


        
        '''
        temp_list = {}
        infile = open("dict_url_names_boston.txt", "a")
        for url in list_restaurants:
            total_count -= 1
            print 'Total # of restaurants left: ', total_count
            temp_list = call_url(url)
            for x, y in temp_list.items():
                full_list[x] = y
                try:
                    print 'Writing to file.'
                    infile.write(x + "," + y + "\n")
                    print 'Done.'
                except:
                    pass
        ''' 
        '''
        i = 2
        while(i <= 81):
            url = "http://www.austinchronicle.com/gyrobase/Guides/restaurant?page="+str(i)+""
            list_restaurants = call_url(url)
            for x in list_restaurants:
                full_list.append(x)
            i += 1
        '''
            
        

        #have a dictionary with {Restaurant_name, Restaurant_menu_url}
        '''
        for x, y in full_list.items():            
            try:
                #print x, y
                infile.write(x + "," + y + "\n")
                #print 'happend'
            except:
                print 'Didn\'t Happen. SOL.'
                pass
        '''

main()    
