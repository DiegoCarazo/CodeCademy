class BankAccount:
  balance = 0
  def __init__(self, name):
    self.name = name #Who the account belongs
  
  def __repr__(self):
    # what reprecents the printed object
    return self.name + ' has an available balance of: ' + str(self.balance) 
  
  def show_balance(self):
    print("The balance in your account is: " + str(self.balance))
  
  def deposit(self, amount):
    if amount <= 0:
      print("Insert a correct amount")
      return
    else:
      print("The deposited amount is: " + str(amount))
      self.balance += amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print("The insufficient balance")
      return
    else:
      self.balance -= amount
      self.show_balance()

my_account = BankAccount('Diego')
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(500)
print(my_account)
