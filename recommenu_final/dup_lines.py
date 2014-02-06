lines_seen = set() # holds lines already seen
'''
outfile = open("boston_fsid_reduced.txt", "w")
for line in open("restaurant_id_and_name.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
'''
outfile = open("boston_fsid_final_reduced.txt", "w")
for line in open("boston_fsid_final.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
