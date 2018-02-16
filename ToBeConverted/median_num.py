"""
median

Great work! You've covered a lot in these exercises. 
Last but not least, let's write a function to find 
the median of a list.

The median is the middle number in a sorted sequence 
of numbers.

Finding the median of [7, 12, 3, 1, 6] would first 
consist of sorting the sequence into [1, 3, 6, 7, 12] 
and then locating the middle value, which would be 6.

If you are given a sequence with an even number of 
elements, you must average the two elements 
surrounding the middle.

For example, the median of the sequence [7, 3, 1, 4] 
is 3.5, since the middle elements after sorting the 
list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() 
function, like so:

sorted([5, 2, 3, 1, 4])

[1, 2, 3, 4, 5]
"""

entry = [4, 5, 5, 4]

def median(entry):
  new_list = []

  for num in entry: #add each num into the new_list
      new_list.append(num)

  new_list.sort() #sort the list numerically
  div = len(new_list) #assign the length of the list 

  if div == 1: #if only one item in list, the median would be 1
    return 1
  elif div % 2 != 0: #if the list isn't even, divide the length by 2
    mid_index = new_list[div / 2] #since indexes start at 0, you don't need to =1
    return mid_index #for example [2,4,6,8,10]. 5 numbers, 5 / 2 = 2 (int). new_list[2] would return 3rd value
  else:					#if list has an even number, use same method as odd (but minus 1) to find out first number
    frst = new_list[(div / 2)-1] #then use the odd method to find the second number
    scnd = new_list[div / 2]
    avg = float(frst + scnd) / 2.0 #add the two values together then divide by 2 to work out median
    return avg
  
print median(entry)