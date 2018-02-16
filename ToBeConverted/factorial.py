"""
To calculate the factorial of a non-negative integer x, 
just multiply all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
"""

def factorial(x):
	x = int(x) #convert to integer
	start = x	#start with int entered as argument
	while x > 1: #whilst x is greater than 1, start loop (greater than one to stop int being mulitplied by 0)
		start *= (x - 1) #multiply with itself - 1
		x -= 1 #amend variable to -1 and reiterate loop until < 1
	return start

print factorial(12)