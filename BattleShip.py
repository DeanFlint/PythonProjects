from random import randint

def game():
  print " ----  Welcome ------"
  print " ----  to  ----------"
  print " ----  battleship  --"
  print " "
  board = []
  complete_line = []
  top_line = ["    ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
  line = 1

  for x in range(10):  # rows
    if x <= 8:
      funct = [str(line) + "   "] + ["0"] * 10
      board.append(funct)
      line = line + 1
    else:
      funct = [str(line) + "  "] + ["0"] * 10
      board.append(funct)
      line = line + 1

  def print_board(board):
    print " ".join(top_line)
    print " "
    for row in board:
      print " ".join(row)
    print " "

  print_board(board)

  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  ship1_row1 = random_row(board) #first 
  ship1_col1 = random_col(board) #ship

  ship2_row1 = random_row(board) #second
  ship2_col1 = random_col(board) #ship - first half

  play_again = 0

  def ship_second_row(row, col):
    direction = randint(0, 2)
    if direction == 0:
      ship2_col2 = col
      ship2_row2 = row - 1
      if ship2_row2 < 0 or ship2_row2 > 9:
        direction()
      return (ship2_row2, ship2_col2) #second ship - second half
    else:
      ship2_col2 = col
      ship2_row2 = row + 1
      if ship2_row2 < 0 or ship2_row2 > 9:
        direction()
      return (ship2_row2, ship2_col2) #second ship - second half
      
  def ship_second_col(row, col):
    direction = randint(0, 2)
    if direction == 0:
      ship2_row2 = row
      ship2_col2 = col - 1
      if ship2_col2 < 0 or ship2_col2 > 9:
        direction()
      return (ship2_row2, ship2_col2) #second ship - second half
    else:
      ship2_row2 = row
      ship2_col2 = col + 1
      if ship2_col2 < 0 or ship2_col2 > 9:
        direction()
      return (ship2_row2, ship2_col2) #second ship - second half
      
  if ship2_row1 == ship1_row1 and ship2_col1 == ship1_col1: # check to make sure ships aren't on top of each other
    ship2_row1 = random_row(board)
    ship2_col1 = random_col(board)
    if ship2_row1 == ship1_row1 and ship2_col1 == ship1_col1: #another check for added security
      ship2_row1 = random_row(board)
      ship2_col1 = random_col(board)

  direction = randint(0, 2)
  if direction == 0:
    ship2_row2, ship2_col2 = ship_second_row(ship2_row1, ship2_col1)
  else:
    ship2_row2, ship2_col2 = ship_second_col(ship2_row1, ship2_col1)

  if ship1_row1 == ship2_row2 and ship1_col1 == ship2_col2: # check to make sure ships aren't on top of each other
    direction()
    if ship1_row1 == ship2_row2 and ship1_col1 == ship2_col2: #another check for added security
      direction()
      
  """ ----SHIP LOCATION FOR TESTING ---  
  #print "Ship 1 row: " + str(ship1_row1)
  #print "Ship 1 col: " + str(ship1_col1)
  #print "Ship 2 row1: " + str(ship2_row1)
  #print "Ship 2 col1: " + str(ship2_col1)
  #print "Ship 2 row2: " + str(ship2_row2)
  #print "Ship 2 col2: " + str(ship2_col2)
  """

  def input_check(r_input):
    if r_input == "":
      print " --------------------------- "
      print "Entry blank, please try again"
      print " --------------------------- "
    elif r_input < 0 or r_input > 9:
      print " --------------------------- "
      print "Needs to be between 1 - 10"
      print " --------------------------- "
    else:
      return True

  for turn in range(10):
    try:
      guess_row = int(raw_input("Guess Row: "))
      guess_col = int(raw_input("Guess Col: "))
    except ValueError:
      print " ----------------------- "
      print "This needs to be a number"
      print " ----------------------- "
    
    if input_check(guess_row) == True and input_check(guess_col) == True:
      guess_row = guess_row - 1
      guess_col = guess_col 
      if guess_row == ship1_row1 and guess_col == ship1_col1 or guess_row == ship2_row1 and guess_col == ship2_col1 or guess_row == ship2_row2 and guess_col == ship2_col2:
        print " -=- "
        print " HIT! "
        print " -=- "
        board[guess_row][guess_col] = "H"
        
        if (board[ship1_row1][ship1_col1] == "H") and (board[ship2_row1][ship2_col1] == "H") and (board[ship2_row2][ship2_col2] == "H"):
          print " -------------------------------- "
          print "You win, you've sunk all battleships!"
          print " -------------------------------- "
          print_board(board)            
          restart()
        else:
          print_board(board)
          
      else:
        if(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "H"):
          print " ----------------------------- "
          print "You've guessed that one already."
          print " ----------------------------- "
        else:
          print " ---- "
          print " MISS "
          print " ---- "
          board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print "Turns remaining: ", 9 - turn
        print " "
        if turn == 9:
          print " ------ "
          print "Game Over"
          print " ------ "
          print_board(board)
          restart()        
        print_board(board)

def restart():
  answer = raw_input("Would you like to play again? ")
  if answer == "Y":
    game()
  else:
    print "Thanks for playing!"

game()