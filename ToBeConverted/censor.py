"""
	 Write a function called censor that takes two strings, text 
	 and word, as input. It should return the text with the word 
	 you chose replaced with asterisks. For example:

	    censor("this hack is wack hack", "hack")

     should return:

	    " this **** is wack **** "
 
 	 Assume your input strings won't contain punctuation or 
	 upper case letters. The number of asterisks you put should 
	 correspond to the number of letters in the censored word.
"""

text = "this hack is wack hack"
word = "hack"

new_list = []

def censor(text, word):
  if word in text.split(): #split the words out of text
    new_list.append(word) #add the word to the empty list
  new_word = "*" * len(word) #replace letters to ' * '
  if word in text: #using the word as an identifier...
    return text.replace(word, new_word) #...replace old word with the new word of ' * '
   
print censor(text, word)