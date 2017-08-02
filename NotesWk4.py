# +---+---+---+---+---+
# | H | e | l | l | o |
# +---+---+---+---+---+
#   0   1   2   3   4
#  -5  -4  -3  -2  -1

phrase = "Tim Smith eats blueberries."
#print phrase[4:9] # Smith
#print phrase[4:] #  Smith eats blueberries.
#print phrase[:9] # Tim Smith
#print phrase[:] # Tim Smith eats blueberries.
#print phrase[-12:] # blueberries
#print phrase[-12:-8] # blue.

mylist = ["A" , "B" , "C" , "D"] 
#print mylist[:2] # 'A', 'B'

nums = range(1, 10)
twice = []
for n in nums:
    if n > 4:
        twice.append(n * 2)

print twice
twice = [n * 2 for n in nums if n > 4]
#print nums
#print twice

list = [98, 77, 87, 93, 66]
newList = sorted(list)
#print newList
newList = sorted(list, reverse = True)
#print newList

d = {'Math' : 98, 'English' : 77, 'Python' : 87, 'Circuit' : 93, 'Yoga' : 66}
newD = sorted(d)
#print newD
newD = sorted(d, reverse = True)
#print newD

x = 4 % 2 # = 0
y = 5 % 2 # = 1
#print "%s %s" %(x, y)

#print "Enter a number:",
#num = int(raw_input())
#if num % 2 == 0:
   # print "Even"
#else:
   # print "Odd"
   
l = ['A','B','C','D','E','F']
for i in range(0, len(l)):
    if (i % 2 == 0):
        print l[i]

p = range(0, 10)
for a in p:
    if a % 2 == 0:
        print a
        
lnew = [a for a in p if a % 2 == 0]
print lnew

