#Introduction to lists
zoo_animals = ["pangolin", "cassowary", "sloth", ];
# One animal is missing!

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])

#Access by Index
numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")

#Acccess list and assign variables
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "lion"

#List length
suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shirt")
suitcase.append("pants")
suitcase.append("shoes")

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)

#List slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last = suitcase[4:6]

#slicing strings
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

#searching for an item in a list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print(animals) # Observe what prints after the insert operation

#Do something for every item in a list
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
  # Your code here
  print(2 * number)

#More with for
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print(square_list)

#accessing items in a dictionary
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin'])# Prints Puffin's room number

# Your code here!
print(residents['Sloth'])
print(residents['Burmese Python'])

#Mutable dictionaries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

#Changing dictionaries
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'

print(zoo_animals)

#Removing from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

#dictionaries mini-project
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

#Practice exercise - for loops in lists
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print(name)

#Practice exercise - for loops in dictionaries
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for word in webster:
  print(webster[word])

#For loop actions on different variables

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print(number)

#Lists and functions
# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

#String looping
for letter in "Codecademy":
  print
  letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print(letter)

#Shopping at the supermarket

shopping_list = ["banana", "orange", "apple"]

prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print(key)
  print("price: %s" % prices[key])
  print("stock: %s" % stock[key])

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total



