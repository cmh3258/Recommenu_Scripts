'''

Script to get the restaurnats that werre already found

Chris Hume
Recommenu
1/20/14

'''

infile = open("boston_fsid_final_chains4.txt","r")
#inf = open("fsname_yelpurl_austin_2.txt","r")
outf = open("boston_fsid_final_chains5.txt","a")

for line in infile:
    sub = line.split(",")
    name = sub[1].strip().lower()
    fsid = sub[0].strip()

    inf = open("item_ratings_boston_new3.txt","r")
    find = False
    for nextl in inf:
        nextl = nextl.split(",")
        rid = nextl[3].strip().lower()

        if rid == fsid:
            print rid, " : ", name
            find = True
            break
            
    if find == False:
        outf.write(fsid + "," + name + "\n")
        print 'writing'
    inf.close()
   # print 'fd'



infile.close()
#inf.close()
