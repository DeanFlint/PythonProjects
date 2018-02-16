"""
This program will:
- Prompt the user to select a shape
- Depending on the shape the user selects, calculate the area of that shape
- Print the area of that shape to the user
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is booting up..."

month = datetime.now().month
day = datetime.now().day
year = datetime.now().year
hour = datetime.now().hour
minute = datetime.now().minute

current = "%s/%s/%s %s:%s" % (month, day, year, hour, minute)
print current

sleep(1)

hint = "Hint: Don\'t forget to include the correct units! \n Exiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Please enter the radius: "))
  area = pi * radius ** 2
  print "Mmm, smell that?"
  sleep(1)
  print "The pie is baking..."
  sleep(1)
  print "The radius of this delicious pie is %.2f. \n%s" % (area, hint)
elif option == "T":
  base = float(raw_input("Please enter the base of the triangle: "))
  height = float(raw_input("Please enter the height of the triangle: "))
  area = 0.5 * base * height
  print "Uni Bi Tri"
  sleep(1)
  print "The area of this magical triangle is %.2f. \n%s" % (area, hint)
else:
  print "You have entered garbage, how very dare you!"