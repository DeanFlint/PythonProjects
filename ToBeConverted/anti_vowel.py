"""
Define a function called anti_vowel that takes one string, 
text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!". 
Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.
"""

vowels = "aeiouAEIOU"
text = str(raw_input("Enter text: "))
array = []

def anti_vowel(text):
  for letter in str(text):
    array.append(letter)
    continue
  array_len = len(array) -1
  while array_len >= 0:
    if array[array_len] not in vowels:
      array_len -= 1
    elif array[array_len] in vowels:
      del array[array_len]
      array_len -= 1
    else:
      continue
  new_string = ''.join(str(e) for e in array)
  return new_string

print anti_vowel(text)


"""
def anti_vowel(text):
    string = ''
    for i in text:
        if i not in "aeiouAEIOU":
            string += i
    return string
"""