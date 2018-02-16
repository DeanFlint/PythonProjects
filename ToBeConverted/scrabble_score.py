"""
Scrabble is a game where players get points by spelling words. 
Words are scored by adding together the point values of each 
individual letter (we'll leave out the double and triple letter 
and word scores for now).

To the right is a dictionary containing all of the letters in 
the alphabet with their corresponding Scrabble point values.

For example: the word "Helix" would score 15 points due to the 
sum of the letters: 4 + 1 + 1 + 1 + 8.
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

word = raw_input("Enter word: ")
word = word.lower() #convert entry to lowercase
matches = [] 

def scrabble_score(word): 
  for letter in word: #for each letter in the word
    found = score.get(letter) #iterate each letter and return value from list
    matches.append(found) #add the values to match list
  total_score = 0
  for letter_value in matches: #add values together
    total_score += letter_value
  return total_score

print scrabble_score(word)


"""better solution:

========================================================
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
     "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
     "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
     "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
     "x": 8, "z": 10}

word = raw_input("Enter word: ")
     
def scrabble_score(word):
    total = 0
    for char in word.lower():
        total += score[char]
    
    return total
  
print scrabble_score(word)
========================================================
"""