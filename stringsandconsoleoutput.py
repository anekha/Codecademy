#Strings
brian = "Hello life!"

#Practice strings
# Assign your variables below, each on its own line!
caesar = 'Graham'
praline = 'John'
viking = 'Teresa'

# Put your variables above this line
print(caesar)
print(praline)
print(viking)

#Escaping characters
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

#Access by Index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print(fifth_letter)

#String methods
parrot = "Norwegian Blue"
len(parrot)
print(len(parrot))

#lower()
parrot = "Norwegian Blue"

print(parrot.lower())

#str method
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print(str(pi))

#Dot notation
ministry = "The Ministry of Silly Walks"

print(len(ministry))
print(ministry.upper())

#Print strings
"""Tell Python to print "Monty Python"
to the console on line 4!"""

print("Monty Python")

#Print variables
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print(the_machine_goes)

#String Concatenation
# Print the concatenation of "Spam and eggs" on line 3!

print("life " + "of " + "Brian")
print("Spam " + "and " + "eggs")

#Explicit String Conversion
# Turn 3.14 into a string

print("The value of pi is around " + str(3.14))

#String Formatting with %
string_1 = "Camelot"
string_2 = "place"

#print("Let's not go to %s. 'Tis a silly %s.") % (string_1, string_2)

#String Formatting with %
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))

#Typing different strings
my_string = "positivity all the way"
print(len(my_string))
print(my_string.upper())

#date and time
from datetime import datetime
now  = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print(now.year)
print(now.month)
print(now.day)

#Print date and time in a specific format
from datetime import datetime
now = datetime.now()
print('%02d-%02d-%04d' %(now.month, now.day, now.year))
print('%02d/%02d/%04d' %(now.month, now.day, now.year))

#Print Date and time
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d %02d:%02d:%02d'%(now.day, now.month, now.year, now.hour, now.minute, now.second))

