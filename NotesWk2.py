# Module/Function Notes
import Ld

#kmWeekday = Ld.userFlt("How many KM did you travel on a weekday?")
#kmWeekend = Ld.userFlt("How many km did you travel on a weekend?")

#miWeekday = Ld.kmToMi(kmWeekday)
#miWeekend = Ld.kmToMi(kmWeekend)

#dollarsWeekday = miWeekday * 0.13
#dollarsWeekend = miWeekend * 0.24

#print "Weekday %.2f" % dollarsWeekday
#print "Weekend %.2f" % dollarsWeekend
#print "Total %.2f" % (dollarsWeekday + dollarsWeekend)

# You Try It 03

#adj01 = Ld.userStr("Enter an adjective:")
#adj02 = Ld.userStr("Enter another adjective:")
#pn01 = Ld.userStr("Enter a plural noun:")
#pn02 = Ld.userStr("Enter another plural noun:")
#celeb = Ld.userStr("Enter a celebrity:")
#noun = Ld.userStr("Enter a noun:")

#print("In the shadowy world of spies, a/an %s organization like the"
#    " US Government uses spies to infiltrate %s groups for the purpose"
#    " of obtaining top secret %s. A teacher, %s or even the little old %s"
#    " with a cane and fifteen pet %s could be a spy.") %(adj01, adj02, pn01, celeb, noun, pn02)

#dayCourses = ['Yoga', 'Calc 3', 'History']
#eveCourses = ['Python']
#allCourses = dayCourses + eveCourses

#print "Day Courses: %s" %dayCourses
#print "Evening Courses: %s" %eveCourses
#print "All Courses: %s" %allCourses

#dayCourses.insert(1, 'Philosophy')
#print "Day Courses: %s" %dayCourses

#del dayCourses[2]
#print "Day Courses: %s" %dayCourses

#eveCourses[0] = 'Introduction to Python'
#print "Evening Courses: %s" %eveCourses

#songPt1 = ['Mary', 'had', 'a']
#songPt2 = (['little', 'lamb'] * 3)
#song = songPt1 + songPt2

#print song

#word = Ld.userStr("Please enter a word:")

#for letter in word:
#    letter = letter + " "
#    print letter,
    
#print "\nAll Done!"

#words = ['Cat', 'Dog', 'Apple', 'House', 'Chicken']
#lengths = []

#for word in words:
#    l = len(word)
#    lengths.append(l)

#print "Here are the lengths %s" %lengths

# You Try it 4

userRtg = []
iceCream = ['Vanilla', 'Chocolate', 'Strawberry', 'Bacon']
for flavor in iceCream:
    Rtg = Ld.userStr("Rate %s from 1 to 5:" % flavor)
    userRtg.append("%s rated as a %s" % (flavor, Rtg))
print userRtg

#trial = []
#trial.append(song[0]);
#trial.append(song[1])
#trial.append(song[2])
#trial.append(song[3])
#trial.append(song[4])
#trial.append(song[5])
#trial.append(song[6])
#trial.append(repetition*(n+1))

#print trial


    