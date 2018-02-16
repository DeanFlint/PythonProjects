"""
In this project, we'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

-View the calendar
-Add an event to the calendar
-Update an existing event
-Delete an existing event

The program should behave in the following way:
1. Print a welcome message to the user
2. Prompt the user to view, add, update, or delete an event on the calendar
3. Depending on the user's input: view, add, update, or delete an event on the calendar
4. The program should never terminate unless the user decides to exit
"""

from time import sleep, strftime

name = "Dean"
calendar = {}

def welcome():
  print "Greetings " + str(name) + "!"
  sleep(1)
  print "Your calendar is loading..."
  sleep(1)  
  print strftime('%A %d, %B %Y')
  print strftime('%H:%M:%S')
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = str(raw_input("A to Add, U to Update, V to view, D to Delete or X to Exit: "))
    user_choice = user_choice.upper()
    
    if user_choice == "V":
      if len(calendar.keys()) == 0:
        print "Calendar is empty"
      else:
        print calendar
        
    elif user_choice == "U":
      date = str(raw_input("What date? "))
      update = str(raw_input("Enter the update: "))
      calendar[date] = update
      sleep(1)
      print "Update successful! :)"
      print calendar
      
    elif user_choice == "A":
      event = str(raw_input("Enter event: "))
      date = str(raw_input("Enter date (MM/DD/YYYY): "))
      if len(date) > 10 or int(date[6:10]) < int(strftime('%Y')):
        print "An invalid date was entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
                                               
    elif user_choice == "D":
      if len(calendar.keys()) == 0:
        print "Calendar is empty"
      else:
        event = str(raw_input("What event? "))
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
          else:
            print "Incorrect date specified"
            
    elif user_choice == "X":
      start = False
      
    else:
      "Invalid command, program terminating"
      
start_calendar()
