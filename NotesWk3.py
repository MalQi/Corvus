#print "How many times should I say hello?"
#t = int(raw_input())

#a = range(0, t)
#for i in a:
#    print "Hello"
    
#l = ['a', 'b', 'c', 'd', 'e']
#for i in range(1,4):
#    print l[i]
    
#s = "A-B-C-D-E"
#m = s.split('-')
#print m

#for line in open('test.txt'):
#    temp = line.split(',')
#    name = temp[0].strip() # strip subtracts the space in the line
#    age = temp[1].strip()
#    print "Name: " + name
#    print "Age: " + age

# a = range(start number, last number - one)
# a = range(x, y, the incremented multiple or backwards if written with a negative)

#d = {"Tim" : ['red', 'blue'], "Sally" : ['blue', 'green', 'yellow']}
#print d["Tim"]
#print d["Sally"]

#print d["Tim"][0]

#print d.values()
#print d.keys()
#print 'Tim' in d
#print len(d)

#for k in d.keys():
#    print "%s -> %s" %(k, d[k])

#v = {}
#for line in open('test.txt'):
#    temp = line.split(',')
#    name = temp[0].strip()
#    age = temp[1].strip()
#    v[name] = age
#print "%s %s" %(v.keys(), v.values())

#print "Enter a name:",
#n = raw_input()
#print v[n]

#*************************#
#****YOU TRY IT***********#

#import Ld

#d = {}
#for line in open("test.txt"):
#    temp = line.split(":")
#    name = temp[0].strip()
#    grades = temp[1].split(",")
#    for index in range(0, len(grades)):
#       grades[index] = grades[index].strip()
#    d[name] = grades
    
#n = Ld.userStr("Enter a name:")
#if n in d:
#    print d[n]
#else:
#    print "%s is not in the file." % n

#*************************#
#****** WEEK  FIVE *******#
#*************************#

#****** WHILE LOOPS ******#
import Ld

#def main():
#    keepGoing = True
#    while keepGoing:
#        msg = Ld.userStr("Enter a Message (enter quit to exit):")
#        if msg == "quit":
#            keepGoing = False
#        else:
#           print msg
#main()

#****** RANDOM NUMBERS ******#
#import random, Ld

#print random.randrange(1, 5)

#def main(counter = 0):
#    ans = random.randrange(1, 11)
#    keepGoing = True
#    while keepGoing:
#        guess = Ld.userInt("Enter a guess from 1 to 10:")
#        if guess == ans:
#            print "You Win!"
#            keepGoing = False
#            counter = counter + 1
#            print "It took you %s guesses." %(counter)
#        elif guess >= ans:
#            print "Guess Lower!"
#        else:
#            print "Guess Higher!"
#        counter = counter + 1
            
#main()

#****** PRICE IS RIGHT ******#
import random, time, Ld

def main():
    # initialize prizes...
    good_prizes = ["New Car!", "$100", "A Badge in Python Class", "Free A!"]
    bad_prizes = ["Old Sock", "Smelly Garbage Can", "Sore Throat", "More Homework"]
    
    # create a list for the doors...
    doors = ["", "", ""]

    # place a random bad prize behind all three doors...
    random.shuffle(bad_prizes)
    doors[0] = bad_prizes[0]
    doors[1] = bad_prizes[1]
    doors[2] = bad_prizes[2]
    
    # replace a random bad prize with a good one...
    random.shuffle(good_prizes)
    iGoodPrize = random.randrange(0,3)
    doors[iGoodPrize] = good_prizes[0]
    
    # let the user pick a door
    door = Ld.userInt("Pick a door (1-3):")
    print "You win a.."
    #time.sleep(5)
    print "... %s" %(doors[door-1])
    
main()