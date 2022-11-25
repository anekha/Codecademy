#control flow
def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()

clinic()

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 4 <3

# Make me true!
bool_three = 3==3

# Make me false!
bool_four = 18 > 19

# Make me true!
bool_five = 3==3

#boolean operator and returns True when the expressions on both sides of and are true
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

#boolean operator or returns True when at least one expression on either side of or is true
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1

#boolean operator not returns True for false statements and False for true statements
bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False

#This and That (or This, But Not That!)
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = True and True

# Make me false!
bool_three = False and True

# Make me true!
bool_four = not False

# Make me true!
bool_five = True or True

#Conditional Statement Syntax
response = "Y"

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

#practice if functions
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print(using_control_once())
print(using_control_again())

#The else statement complements the if statement
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False       # Make sure this returns False

#elif function
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))


# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))

#starting to build a pig latin translator
print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")

#Building a functioning Pig Latin translator
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
else:
    print('empty')

