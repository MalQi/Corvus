# Wade Hasty
# 11JUL17
# Program for Intro to Python Course
# This program allows the User to input a recipe for bread

# Asks User for Ingredients
print "Enter the amount of Flour (cups):",
flour = raw_input()
print "Enter the amount of Water (cups):",
water = raw_input()
print "Enter the amount of Salt (teaspoons):",
salt = raw_input()
print "Enter the amount of Yeast (teaspoons):",
yeast = raw_input()

# Asks User for Adjustments and Calculates Modified Recipe
print "Enter the loaf adjustment factor (e.g. 2.0 doubles the size):",
factor = raw_input()
print "-- Modified Recipe --"
print "Flour: %.2f cups." %(float(flour) * float(factor))
print "Water: %.2f cups." %(float(water) * float(factor))
print "Salt: %.2f teaspoons." %(float(salt) * float(factor))
print "Yeast: %.2f teaspoons." %(float(yeast) * float(factor))
print "Happy Baking!"
