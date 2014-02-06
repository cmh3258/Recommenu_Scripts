'''

Go through restaurants that has no fs menus, then
see if the venue is actually a restaurant

Chris Hume
Recommenu
1/25/14


'''

def load_nomenu_done():
    in3 = open("rest_hasnone_austin.txt", "r")
    dict1 = {}
    for line in in3:
        line = line.strip()
        line = line.strip('')
        arr = line.split(",")
        fsid = arr[0].strip()
        dict1[fsid] = ''
    in3.close()

    #for x,y in dict1.items():
    #    print x
    return dict1
    

def load_alreadydone():
    in4 = open("rest_not_restaurant_austin.txt","r")
    dict2 = {}
    for line in in4:
        line = line.strip()
        arr = line.split(",")
        fsid = arr[0].strip()
        dict2[fsid] = ''
    in4.close()
    return dict2
    
def main():

    in1 = open("restaurant_nomenu_austin2.txt","r")
    in2 = open("menu_final_austin.txt", "r")

    for line in in1:
        #print 'start..'
        line = line.strip()
        line = line.strip('\n')
        #print line
        arr = line.split(" ")
        dict1 = load_nomenu_done()
        dict2 = load_alreadydone()
        
        if len(arr) <= 1 and line != '':
            fsid = line.strip()
            if dict1.has_key(fsid):
                print 'found ', fsid
                continue
            if dict2.has_key(fsid):
                print 'found2 ', fsid
                continue

            #print 'i get here'        
    
            in2 = open("menu_final_austin.txt", "r")
            out = open("rest_hasnone_austin.txt","a")
            out2 = open("rest_not_restaurant_austin.txt" , "a")
            for nline in in2:    
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
    
main()
