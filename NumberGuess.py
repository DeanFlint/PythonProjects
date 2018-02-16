"""
The program should do the following:
  -Randomly roll a pair of dice
  -Add the values of the roll
  -Ask the user to guess a number
  -Compare the user's guess to the total value
  -Decide a winner (the user or the program)
  -Inform the user who the winner is
"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: " + str(max_val)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "Your guess exceeds the maximum possible value..."
  else:
    print "Rolling..."
    sleep(2)
    print "First roll: %d" % (first_roll)
    sleep(1)
    print "Second roll: %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total: %d" % (total_roll)
    print "Result...."
    sleep(1)
    if user_guess > total_roll:
      print "You won! :D"
    else:
      print "You lost :/"

roll_dice(6)