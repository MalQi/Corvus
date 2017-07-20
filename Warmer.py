# Author: Wade Hasty
# Intro to Python
# 18 JUL 17
# This program assesses temperature anomalies

# Read the Temps from the file
# And Returns them in a list
def readTemps(dev):
    file = open('nasa.txt')
    for line in file:
        dev.append(float(line))

# calculates the average of a range of numbers
# as specifically by start (inclusive) and stop (inclusive)
def calculateAve(temps, start, stop):
    index = 0
    total = 0.0
    for t in temps:
        if (index >= start and index < stop):
            total = total + t
        index = index + 1
    return total/(stop-start) 

# counts all values that have a positive deviation
# in the range as specified by start (inclusive)
# and stop (inclusive)
def count(temps, start, stop):
    index = 0
    c = 0
    for t in temps:
        if (index >= start and index < stop):
            if t > 0.0:
                c = c + 1
        index = index + 1
    return c
    
# main function
# data downloaded from http://climate.nasa.gov/
# data represents the deviation in a global surface
# temperature relative to 1951 - 1980 average temperatures.
def main():
    myTemps = []
    readTemps(myTemps)
    ave7 = calculateAve(myTemps, 0, 80)
    cnt7 = count(myTemps, 0, 80)
    print "During the first 81 years, the average deviation from the temperature anomaly is %s" %ave7
    print "During the first 81 years, %s had a positive temperature anomaly" %cnt7
    ave3 = calculateAve(myTemps, 81, 116)
    cnt3 = count(myTemps, 81, 116)
    print "During the last 35 years, the average deviation from the temperature anomaly is %s" %ave3
    print "During the last 35 years, %s had a positive temperature anomaly" %cnt3
    
main()