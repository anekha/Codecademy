#printing the data
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for i in grades_input:
    print(i)

print_grades(grades)

#the sum of scores
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  count = 0
  for i in scores:
    count += i
  return count

print(grades_sum(grades))

#the average of scores
def grades_average(grades_input):
  sum = grades_sum(grades_input)
  count = float(len(grades_input))
  grades_average = sum/count
  return grades_average

print(grades_average(grades))

#the variance of scores
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)


print(grades_variance(grades))

#calculating the standard deviation
def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print(grades_std_deviation(variance))

#printing the statistics
for grade in grades:
  print(grade)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
