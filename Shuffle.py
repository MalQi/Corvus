# Program by Wade Hasty
# 1 AUG 17
# Intro to Python
# This program deals five cards
# After shuffling as many times as
# User inputs
#---------------------------------------#
import Ld

#---------------------------------------#
# Takes all the cards and pairs the 
# Suits and ranks together
#---------------------------------------#
def buildDeck(rank, suit):
    deck = []
    for r in rank:
        for s in suit:
            card = "%s of %s" % (r, s)
            deck.append(card)
    return deck

#--------------------------------------#
# Shuffles the deck a varied amount
# Swaps each card from two halves
# After being split-up, Then recreates
# The Deck using Modulo Operator
#--------------------------------------#
def shuffle(deck):
    shuffle = []
    firstHalf = deck[:26]
    secondHalf = deck[27:]
    a = Ld.userInt("How Many Times Would You Like to Shuffle the Deck?")
    p = range(0, a)
    for n in p:
        for l in range(0, 25): #len(deck)):
            #if l % 2 == 0:
            fCard = firstHalf[l]
            shuffle.append(fCard)
            #else:
            sCard = secondHalf[l]
            shuffle.append(sCard)
        shuffle = shuffle[:52]
    return shuffle

#------------------------------#
# Takes the first five cards
# And passes them to the User
#------------------------------#
def deal(deck):
    hand = deck[:5]
    return hand

#-----------------------------#
# Culminates the program
#-----------------------------#
def main():
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    d = buildDeck(rank, suit)
    print d
    s = shuffle(d)
    print s
    hand = deal(s)
    print "\n%s" %(hand)

main()