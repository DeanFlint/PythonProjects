"""
A Python class that can be used to create and manipulate a personal bank account.

The bank account class have the following methods:
- Accepting deposits
- Allowing withdrawals
- Showing the balance
- Showing the details of the account
"""

class BankAccount(object):
  balance = 0
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "This account belongs to %s. The balance of this account is $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "The balance of this account is %.2f" % (self.balance)
  
  def deposit(self, amount):
    self.amount = amount
    if amount <= 0:
      print "Invalid amount"
      return
    else:
      print "You have just made a deposit of %.2f" % (self.amount)
      self.balance += amount
      self.show_balance()
    
  def withdraw(self, amount):
    self.amount = amount
    if amount <= 0 or amount >= self.balance:
      print "Invalid amount"
      return
    else:
      print "You have just made a withdrawal of %.2f" % (self.amount)
      self.balance -= amount
      self.show_balance()
  
my_account = BankAccount("Dean")
print my_account
print my_account.show_balance()
print my_account.deposit(2000)
print my_account.withdraw(1000)
print my_account