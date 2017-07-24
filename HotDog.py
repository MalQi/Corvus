# Program By Wade Hasty
# 24 JUL 17
# Intro to Python
# This is a Hot Dog Eating Contest
# The User inputs a guess and the
# Program randomly chooses a winner
import Ld, random, time

# This section of the code conatains the running loop
# During its operation the random amount of hotdogs 
# (1-5) are consumed and added. The loop stops when someone
# eats greater than 50 hotdogs.
def race(sally = 0, tom = 0, fred = 0, hotDog = 0):
    while(hotDog <= 50):
        sally = sally + random.randrange(1, 6)
        tom = tom + random.randrange(1, 6)
        fred = fred + random.randrange(1, 6)
        print "Sally ate %s so far.." %sally
        print "Tom ate %s so far.." %tom
        print "Fred ate %s so far.." %fred
        if sally > 50:
            print "\nSally Won!"
            hotDog = sally
            winner = "Sally"
        elif tom > 50:
            print "\nTom Won!"
            winner = "Tom"
            hotDog = tom
        elif fred > 50:
            print "\nFred Won!"
            hotDog = fred
            winner = "Fred"
        else:
            print "\nchomp... chomp... chomp...\n"
            time.sleep(3)
    return winner

# This takes the User's guess and
# compares it to the actual result
def bet():
    if (pick == winner):
        print "\nYou Picked Correctly!"
    else:
        print "\nYou Picked Incorrectly!"

# Main Function 
def main():
    print "Ready, Set, Eat!\n"
    race()
    bet()

# Global Variables
winner = ""
pick = Ld.userStr("Pick a winner (Tom, Sally, or Fred)")
main()