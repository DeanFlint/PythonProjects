"""
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. 

In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.

If there is a number between 1 and x that goes in evenly, then x is not prime
"""

x = int(raw_input("please enter your prime number for checking now"))

def is_prime(x):
    if x == 2:
        return True
        print "X equals two, True printed" #TEST CODE
    elif x < 2:
        return False
        print "Program recognises x < 2" #TEST CODE
    elif x == 3:
        return True
        print "X equals three, True printed" #TEST CODE
    elif x > 3:
        print "just before for loop" #TEST CODE
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        return True
print is_prime(x)