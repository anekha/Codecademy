#while loop
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 5:
  print("Hello, I am a while and count is", count)
  count += 1

#conditional statements
loop_condition = True

while loop_condition:
  print("I am a loop")
  loop_condition = False

#using the while loop
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print(num ** 2)
  # Increment num (make sure to do this!)
  num += 1

#using while loop for simple errors
choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")

#fixing infinite loops
count > 0

#while count < 10: # Add a colon
#  print(count)
  # Increment count

#Break statements
count = 0

while True:
  print(count)
  count += 1
  if count >= 10:
    break

#using while/else
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")

#making a game with while/else
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")

#the for loop
print("Counting...")

for i in range(20):
    print(i)

#appending to a list
hobbies = []

# Add your code below!

for num in range(3):
  hobby =  input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print(hobbies)

#using for loops to go through a list
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)

# Add your loop below!
for num in numbers:
  print(num ** 2)

#looping over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print(key, d[key])

#counting as you go
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index, item)

#iterate over multiple lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
    print(max(a, b))

#loops with for and else
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', f)
else:
  print('A fine selection of fruits!')

#for and else with a break
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
  print('A', f)
else:
  print('A fine selection of fruits!')

#creating an even function
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(900))

#determine if its an integer
def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

#creating a digital sum

def digit_sum(n):
    total = 0
    string_n = str(n)
    for char in string_n:
        total += int(char)
    return total


# Alternate Solution:

# def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total

print(digit_sum(1234))

#the factorial
def factorial(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total


print(factorial(5))

#creating a function to find the prime
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(13))
print(is_prime(10))

#making a reverse function
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word


print(reverse("Hello World"))

#creating an anti-vowel function
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print(anti_vowel("hello book"))

#scrabble score calculator
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        for leter in score:
            if letter == leter:
                total = total + score[leter]
    return total


print(scrabble_score("pizza"))

#a censor function
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)

    return result


print(censor("this hack is wack hack", "hack"))

#a count function
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count


print(count([1, 2, 1, 1], 1))

#filtering through a list
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res


print(purify([1, 2, 3, 4]))

#a product function to remove duplicates
def remove_duplicates(inputlist):
    if inputlist == []:
        return []

    # Sort the input list from low to high
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)

    return outputlist


print(remove_duplicates([1, 1, 2, 2]))

