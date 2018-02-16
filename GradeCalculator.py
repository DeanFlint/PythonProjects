"""
We've created quite a few meaningful functions. Namely, 
we've created helper functions to print a list of grades, 
compute the sum, average, variance, and standard deviation 
about a set of grades.

Let's wrap up by printing out all of the statistics.

Who needs to pay for grade calculation software when 
you can write your own? :)

Print out the following:
- all of the grades
- sum of grades
- average grade
- variance
- standard deviation
"""
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  avg = grades_average(scores)
  variance = 0
  for score in scores:
    score = (avg - score) ** 2
    variance += score    
  return variance / len(scores)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)