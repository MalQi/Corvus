# Author: Wade Hasty
# Intro to Python
# 16 JUL 17
# This program creates a song

import Ld
song = []
verses = ['First Verse:', 'Second Verse:', 'Third Verse:', 'Fourth Verse:']

# Takes User input for song creation
# First Chorus, then the verses
repetition = Ld.userStr("Enter the Chorus")
n = Ld.userInt("Enter the number of Chorus Repetitions:")
for verse in verses:
    verse = Ld.userStr("Enter the %s" % verse)
    song.append(verse)
    song.append(repetition*n)

# Function that builds the rhythm of the song
def songFun():
    for eachLine in song[:5]:
        print(eachLine)
    song.append(repetition)
    print song[-1] * (n+1)

# Printing the actual aong lyrics
print ""
songFun()
print "\nOne More Time! ...\n"
songFun()