class Category:
  #food, clothin, entertainment
  def __init__(self, name, balance=0):
    self.name = name
    self.balance = balance
    self.ledger = []

  def deposit(self, amount, description=""):
    self.balance += amount
    t_obj = {"amount": amount, "description": description}
    #print(type(t_obj))
    self.ledger.append(t_obj)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      t_obj = {"amount": -amount, "description": description}
      self.ledger.append(t_obj)
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, Category):
    if self.withdraw(amount, "Transfer to " + Category.name):
      Category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if (amount > self.balance):
      return False
    else:
      return True

  def __str__(self):
    res = ""
    star = "*"
    tmp = int((30 - len(self.name)) / 2)
    #print(tmp)
    for i in range(tmp):
      res += star
    return res + self.name + res


def create_spend_chart(categories):
  pass
