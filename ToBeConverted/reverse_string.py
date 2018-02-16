"""
Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.

You may get a string containing special characters (for example, !, @, or #).
"""

array = [] 
new_array = []
text = raw_input(str("Enter Text: "))


def reverse(text):
  for letter in str(text): #iterate through each character of entry
    array.append(letter) #add each characters to the blank list
    continue
  start = len(array) - 1 #length of list - 1 (for indexing)
  while start >= 0: #whilst over or equal to 0...
    new_array.append(array[start]) #... add from array to new array starting from end
    start -= 1 #then reduce the index number by 1 and reiterate
  new_string = ''.join(str(e) for e in new_array) #convert list to string
  return new_string

print reverse(text)