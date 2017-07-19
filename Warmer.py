# Author: Wade Hasty
# Intro to Python
# 18 JUL 17
# This program assesses temperature anomalies

# Read the Temps from the file
# And Returns them in a list
def readTemps():
    file = open('nasa.txt')
    dev = []
    for line in file:
       words = line.split(" ")
       print words  
    

# calculates the average of a range of numbers
# as specifically by start (inclusive) and stop (inclusive)
#def calculateAve(temps, start, stop):
        

# counts all values that have a positive deviation
# in the range as specified by start (inclusive)
# and stop (inclusive)
#def count(temps, start, stop):
    
    
# main function
# data downloaded from http://climate.nasa.gov/
# data represents the deviation in a global surface
# temperature relative to 1951 - 1980 average temperatures.
#def main():
#    temps = readTemps()
    
readTemps()

