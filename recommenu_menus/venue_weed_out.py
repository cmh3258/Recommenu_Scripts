'''

Go through restaurants that has no fs menus, then
see if the venue is actually a restaurant

'''

in1 = open("restaurant_nomenu_austin2.txt","r")
in2 = open("menu_final_austin.txt", "r")


for line in in1:
    line = line.strip()
    arr = line.split(" ")
    if len(arr) <= 1:
        #print line
        fsid = line

        in2 = open("menu_final_austin.txt", "r")
        exist = False
        for nline in in2:
            
            in3 = open("rest_hasnone_boston.txt", "r")
            for x in in3:
                if x.strip() == nline:
                    exist = True
                    break
            in3.close()
            
            in4_open = False
            if exist != True:
                #print 'in here'
                in4 = open("rest_not_restaurant.txt","r")
                in4_open = True
                for x in in4:
                    if x.strip().lower() == nline.strip().lower():
                        #print 'found line'
                        exist = True
                        break
                
            if exist:
               #print 'Already Exist'
                continue
            
            if in4_open == True:
                in4.close()
                
            out = open("rest_hasnone_boston.txt","a")
            out2 = open("rest_not_restaurant.txt" , "a")
            nliner = nline.split(",")
            nfsid = nliner[0].strip()
            nrest = nliner[1].strip()

            if nfsid == fsid:
                #print nline
                print 'Is ', nrest, ' a restaurant?'
                answer = raw_input("y/n = ")
                if answer == 'y':
                    #print 'yes'
                    print 'Saved to Good.'
                    out.write(nline+"\n")
                else:
                    print 'Saved to No_good'
                    out2.write(nline+"\n")
            out.close()
            out2.close()
in1.close()
in2.close()
#out.close()


'''

If we read in the file, then save into a dictionary so then
can just see if it already exist. dict saved by fsid.

'''


