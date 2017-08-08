import Ld

#--------------------------------------|
# Selects a Random Word from a File    |
# And Returns it                       |
#--------------------------------------|

def pickWord():
    return "apples"
    
#--------------------------------------|
# Displays the current board showing   |
# where letters have been guessed      |
#--------------------------------------|
def displayBoard(board):
    for ch in board:
        print "%s " % ch,
    print

#--------------------------------------|
# Asks the User to  guess a letter     |
# And Returns that letter              |
#--------------------------------------|
def askUserForLetter():
    l = Ld.userStr("Please select a letter:")
    return l
#--------------------------------------|
# Given the board, the word, and the   |
# chosen letter, this function checks  |
# to see if the letter is in the word  |
# this returns false, otherwise the    |
# User guessed wrong and true is       |
# returned                             |
#--------------------------------------|
def updateBoard(board, word, letter):
    missed = letter not in word
    # check to see if the letter is in word
    # if it is not, then missed is true
    if letter in word:
        missed = False
    
    # check each letter in word to see if it
    # is the letter the user entered
    # if it is, update the board...
    for i in range(0, len(word)):
        if word[i] == letter:
            board[i] = letter
    
    return missed

#--------------------------------------|
# Returns True if the board no longer  |
# has any * in it, this means all      |
# letters have been guessed            |
#--------------------------------------|
def testForGameOver(board):
    return "*" not in board

def main():
    # Pick a Random word
    word = pickWord()
    
    # initialize the board...
    board = []
    for ea in word:
        board.append('*')
    print board
    
    # initialize the game...
    misses = 0
    gameOver = False
    
    # start main game loop...
    while gameOver != True:
        
        # display the board...
        displayBoard(board)
        
        # let the User guess a letter...
        letter = askUserForLetter()
        
        # update the board if the User misses
        if updateBoard(board, word, letter) == True:
            misses = misses + 1
            print "The word does not contain %s, you have %s misses." % (letter, misses)
        
        gameOver = testForGameOver(board)
    
    # print the end game message
    print "You did it!"
    print "The word is %s" % word
    print "You had %s wrong guesses." % misses

main()