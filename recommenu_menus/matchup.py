'''

Will go through list of chains, and just weed out the bad ones
- will save it to ""

Chris Hume
1/17/14


'''


#this is so janke
openfile = open("list_of_menus_boston.txt", "r")
out = open("matching_good_boston.txt","a")
#openfile = open("list_of_menus_boston.txt", "r")
#out = open("list_of_menus_boston","a")
keep = []

d = {}
yes = no = count = 0
good_word = ''
for line in openfile:
    print 'line: ',line
    line = line.lower().strip()
    if line == 'good':
        #print 'Equals good'
        good_id = openfile.next()
        print 'Equals good: ', good_id
        if good_id.strip().lower() != 'bad':
            print 'Good: ',good_id
            good_word = good_id
            #out.write('good: '+good_id+"\n")
    if line == 'bad':
        bad_menus = True
        while(bad_menus):
            bad_bad = openfile.next()
            print len(bad_bad)
            if len(bad_bad) == 25:
                print 'bad id', bad_bad
                #out.write('bad: '+bad_bad+'\n')
                out.write(good_word.strip() + "," + bad_bad+"\n")
            else:
                bad_menus = False
                print 'didn\'t work: ', bad_bad
                good_word = ''
    
out.close()
openfile.close()
