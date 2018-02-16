"""
Define a function called purify that takes in a list of 
numbers, removes all odd numbers in the list, and returns 
the result. For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; 
instead, return a new list with only the even numbers.
"""

seq = [4, 5, 5, 5, 5, 4]
new_seq = []

def purify(seq):
  for item in seq:
    if item % 2 == 0: # for each item, if the value is 0 when divided by 2...
      new_seq.append(item) # ...add the item to the new empty list.
  return new_seq 
  
print purify(seq)