# Using the print statement
print("Hello, world!")
print("Water; there is not a drop of water there! "
      "Were Niagara but a cataract of sand, would you travel your thousand miles to see it?")

# Printing strings
print("Hello Anekha")
print("This is a good string")
print('You can use single quotes or double quotes for a string')
print("This is " + "a good string")

#Creating variables
todays_date = "04.04.2022"

#Printing remainders
product = 1120 * 6
remainder = 1398%11
print(remainder)

#Updating Variables
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall
annual_rainfall += october_rainfall
annual_rainfall += november_rainfall
annual_rainfall += december_rainfall

print(annual_rainfall)

#Holding numbers in Python
cucumbers = 10
price_per_cucumber = 3.25
total_cost=price_per_cucumber*cucumbers
print(total_cost)

#Two Types of Division
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers/num_people

print(whole_cucumbers_per_person)
float_cucumbers_per_person = float (cucumbers)/num_people
print(float_cucumbers_per_person)

#Multi-line Strings
haiku = """The old pond,
A frog jumps in:
Plop!"""

#Booleans
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

age_is_12 = False
name_is_maria = True

#Data Types
float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
big_string = "The product was " + str(product)
print(big_string)

#Skills Review
skill_completed = "Python Syntax"
exercises_completed = 13
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise
#The amount of points for each exercise may change, because points don't exist yet
print('I got ' + str(point_total) + ' points!')




