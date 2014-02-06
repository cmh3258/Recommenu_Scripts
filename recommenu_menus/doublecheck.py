'''

Will go through list of chains, and just weed out the bad ones
- will save it to ""

Chris Hume
1/17/14


'''


#this is so janke
openfile = open("menu_final_2.txt", "r")

keep = []

d = {}
yes = no = count = 0
for line in openfile:
    line = line.split(",")
    fsid = line[0].strip()
    rest_name = line[1].strip().lower()
    answer = line[2].strip().lower()
    count += 1

    #put restaurant into a hash
    if answer == 'y':
        d[rest_name] = 'y'
        yes += 1
    if answer == 'n':
        rec = d.get(rest_name)
        #only if there isnt a key, then we place a key with no
        #we want to keep the key = 'y' if already exist
        if not rec:
            #print 'none again'
            d[rest_name] = 'n'
        #else:
        #    print 'already exist'

print count
print yes

    
out = open("new_nomenu.txt", "a")
for x, y in d.items():
    if y == 'n':
        print x, y
        out.write(x + "," + y + "\n")

'''
    nomenu = open("no_menu.txt","r")    
    for path in nomenu:
        rest_ne = path.strip().lower()
        if rest_ne == rest_name:
            yes += 1
            ans = dict[rest_name]
            print ans
        else:
            no += 1
        #    print rest_ne, " : ", rest_name
    nomenu.close()
'''
    

out.close()
openfile.close()
#nomenu.close()
'''
for line in nomenu:
    word = line.strip().lower()
    print word
    for x in openfile:
        ray = x.split(",")
        name = ray[1].strip().lower()
        print 'name: ', name , ' word:', word
        rating = ray[2].strip()
        #if find a file that has a yes, then don't need to add it
        if word == name and rating == 'y':
            keep.append(x.lower())
            print 'keeping: ', x
                
nomenu.close()
openfile.close()

nomenu = open("no_menu.txt","r")
for line in nomenu:
    word = line.strip()
    if word in keep:
        print keep
   # else:
    #    print 'not here'

openfile.close()
'''
