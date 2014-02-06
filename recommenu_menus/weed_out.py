'''

Will go through list of chains, and just weed out the bad ones
- will save it to ""

Chris Hume
1/17/14


'''

openfile = open("menu_final_boston.txt", "r")
outfile = open("good_menu_fs_final_boston.txt","a")

for line in openfile:
    ray = line.split(",")
    print ray[2]
    word = ray[2]
    word = word.strip()
    if word == "y":
        outfile.write(line+"\n")

openfile.close()
outfile.close()
