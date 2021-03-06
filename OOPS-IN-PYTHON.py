# OOPS IN PYTHON : Object Oriented Programming

#-------------------------------------------------------#
"""
# State:

Suppose we want to model a bank account with support for
deposit and withdraw operations.

One way to do that is by using global state as shown in
the following example.
"""
# Single Model Bank Account Example
# Creating a Function
balance = 5

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

# Accessing a Function
print(deposit(10))
print(withdraw(20))

"""
The above example is good enough only if we want to have
just a single account.

Things start getting complicated if want to model
multiple accounts.

We can solve the problem by making the state local,
probably by using a dictionary to store the state.
"""
# Multiple Model Bank Account Example
# Creating Functions
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']


# Calling/Accessing Functions
a = make_account()
b = make_account()

print(deposit(a, 100))
print(deposit(b, 50))
print(withdraw(b, 10))
print(withdraw(a, 10))

"""Output:
100
50
40
90"""
#-------------------------------------------------------#
# Classes and Objects :

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Calling/Accessing a class
a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(50))
print(b.withdraw(10))
print(a.withdraw(10))

"""OUTPUT:
100
50
40
90"""
#-------------------------------------------------------#
# Inheritance:

"""
Let us try to create a little more sophisticated account
type where the account holder has to maintain a
pre-determined minimum balance.
"""
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

x=MinimumBalanceAccount()
y=MinimumBalanceAccount()

print(x(10))
print(y(20))
#-------------------------------------------------------#

#-------------------------------------------------------#

#-------------------------------------------------------#


#-------------------------------------------------------#

#-------------------------------------------------------#
