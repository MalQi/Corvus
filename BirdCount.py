# Program by Wade Hasty
# 25 JUL 17
# Intro to Python
# This program asks the User for any Bird
# Then after reading the file
# Tells the User how many times the
# Chosen Bird was seen.

import Ld

#  ------------------------------------------------------------
#  Reads the specified file (filename) and returns a dictionary
#  whose keys are bird names and whose values are the number of
#  times the bird has been seen.
#  ------------------------------------------------------------

def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(',')
        name = temp[0].strip()
        count = int(temp[1].strip())
        if name in d: 
            d[name] = d[name] + count
        else:
            d[name] = count
    return d


#  ------------------------------------------------------------
#  Asks the user to   enter a bird name and then looks up
#  the sighting count for that bird in the specified
#  dictionary (d).
#  ------------------------------------------------------------
def askUser(d):
    birdName = Ld.userStr("Enter a Bird Name:")
    if birdName in d:
        print "%s has been spotted %s time(s)." %(birdName, d[birdName])
    else:
        print "Sorry, That Bird Has Been Spotted 0 Time(s)."
    
    
def main():
    d = countBirds("Birds.txt")
    askUser(d) 
    
main()