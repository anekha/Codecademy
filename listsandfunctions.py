#list accessing
n = [1, 3, 5]

# Add your code below
print(n[1])

#list element modification
n = [1, 3, 5]
# Do your multiplication here
n[1]=n[1]*5
print(n)

#appending to a list
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print(n)

#Removing elements from lists
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print(n)

#Changing the functionality of a function
number = 5

def my_function(x):
    return x * 3

print(my_function(number))

#using more than one argument in a function
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
    return x+y

print(add_function(m, n))

#strings in functions
n = "Hello"
# Your function here!
def string_function(s):
    return s + "world"
print(string_function(n))

#passing a list to a function
def list_function(x):
    return x

n = [3, 5, 7]
print(list_function(n))

#Using an element from a list in a function
def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))

#Modifying an element of a list in a function
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print(list_function(n))

#List manipulation in functions
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst

print(list_extender(n))

#Printing out a list item by item in a function
n = [3, 5, 7]

for i in range(0, len(n)):
    print(n[i])

#Modifying each element in a list in a function
n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print(double_list(n))

#Passing a range into a function
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function([0,1,2])) # Add your range between the parentheses!

#Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

#Using strings in lists in functions
n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))

#Using two lists as two arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!

def join_lists(x, y):
	return x + y


print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]

#Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print(flatten(n))

#Battleships challenge
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print("Game Over")
    print_board(board)