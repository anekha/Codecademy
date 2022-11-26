#iterating over a dictionary
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print(my_dict.items())

#key/value pair from the dictionary
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print(my_dict.keys())
print(my_dict.values())

#the 'in' operator
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print(key, my_dict[key])

#building lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

#List Comprehension Syntax
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print(even_squares)

#testing list Comprehension
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print(cubes_by_four)

#List Slicing Syntax
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l[2:9:2])

#omitting indices
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print(my_list[::2])

#reversing a list
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]

#stride length
to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

#practicing the above
to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]

#functional programming
my_list = range(16)
#print(filter(lambda x: x % 3 == 0, my_list))

#Lambda Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
#print(filter(lambda x: x == "Python", languages))

#testing lambda and filter
squares = [x ** 2 for x in range(1, 11)]

#print(filter(lambda x: x >= 30 and x <= 70, squares))

#iterating over dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())

#list comprehensions
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

#list slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]

#lambda expressions
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
#print(message)

#bitwise operators
print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5) # Bitwise AND
print(9 | 4)  # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT

#The Base 2 Number System
print(0b1),    #1
print(0b10),   #2
print(0b11),   #3
print(0b100),  #4
print(0b101),  #5
print(0b110),  #6
print(0b111)   #7
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)

#counting in binary
print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))

#left and right shift operators
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))

#bitwise AND (&) operator
print(bin(0b1110 & 0b101))

#bitwise OR (|) operator
print(bin(0b1110 | 0b101))

#XOR (^) or exclusive or operator
print(bin(0b1110 ^ 0b101))

#bitwise NOT operator (~)
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)

#bit mask
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

#masks to turn a bit in a number on using |
a = 0b10111011

mask = 0b100
desired = a | mask
print(bin(desired))

#XOR (^) operator
a = 0b11101110

mask = 0b11111111
desired = a ^ mask

print(bin(desired))

#left shift (<<) and right shift (>>) operators
def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)




