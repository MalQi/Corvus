#========================================#
# Program by Wade Hasty                  #
# 7 AUG 17                               #
# Intro to Python                        #
# This program searches through the DIR  #
# For all relevant matchups to the User  #
# Inquiry                                #
#========================================#
import Ld
import os
files = os.listdir(".")

#========================================#
# This function looks at all the text    #
# documents and compiles them into a     #
# searchable dictionary                  #
#========================================#
def compiledTxt(filename):
    d = {}
    for line in open(filename):
        temp = line.split(",")
        word = temp[0].strip()
        count = int(temp[1].strip())
        if word in d: 
            d[word] = d[word] + count
        else:
            d[word] = count
    return d

#========================================#
# Gets User input to search the          #
# Dictionary with.                       #
#========================================#
def askUser(d):
    userWord = Ld.userStr("Enter a search term:")
    if userWord in d:
        print "I found %s result(s)." %(d[userWord])
    else:
        print "Sorry, That Word is not in the File(s)."

#========================================#
# This looks at the whole line           #
# Where the word was found and gives     #
# It back to the User                    #
#========================================#
def linePhrase():
    for line in d:
        if word in d:
            print line

#========================================#
# 1) Loads and Compiles the files        #
# 2) Gets User Input                     #
# 3) Gives Information Asked For         #
#========================================#
def main():
    d = compiledTxt(files)
    askUser(d)
    l = linePhrase()

main()