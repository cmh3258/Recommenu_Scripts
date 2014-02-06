'''

Will go through list of chains, and just weed out the bad ones
- will save it to ""

Chris Hume
1/17/14


'''


#this is so janke
openfile = open("menu_final_boston.txt", "r")

#keep = []

d = {}
yes = no = count = 0
for line in openfile:
    #initiating my list
    main_list = []
    good_list = []
    bad_list = []

    line = line.split(",")
    fsid = line[0].strip()
    rest_name = line[1].strip().lower()
    answer = line[2].strip().lower()
    count += 1

    #put restaurant into a hash
    if answer == 'y':
        #d[rest_name] = 'y'
        #yes += 1
        exist = d.get(rest_name)
        if exist:       #already added
            main_list = d[rest_name]
            good_list = main_list[0]
            bad_list = main_list[1]
       # if not exist:   #hasn't been added yet
        new_list = []
        good_list.append(fsid)
        new_list.append(good_list)
        new_list.append(bad_list)
        d[rest_name] = new_list
        
    elif answer == 'n':
        rec = d.get(rest_name)
        if rec:       #already added
            main_list = d[rest_name]
            good_list = main_list[0]
            bad_list = main_list[1]
       # if not exist:   #hasn't been added yet
        new_list = []
        bad_list.append(fsid)
        new_list.append(good_list)
        new_list.append(bad_list)
        d[rest_name] = new_list

print count
print yes

   
out = open("list_of_menus_boston.txt", "a")
for x, y in d.items():
    #if y == 'n':
    print x
    out.write(x+"\n")
    count = 0
    nono = True
    for sub in y:
        if count == 0:
            print 'Good'
            out.write("Good\n")
        if count == 1:
            print 'Bad'
            nono = False
            out.write("Bad\n")
        for bub in sub:
            print bub
            #if nono == True:
                #out.write(bub + ","+ x +"\n")
            out.write(bub+"\n")
        count += 1
    print '--------'
#        out.write(x + "," + y + "\n")

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
